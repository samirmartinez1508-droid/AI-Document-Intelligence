import pypdf
import json
from io import BytesIO
from fastapi import FastAPI, UploadFile, File, HTTPException
from pypdf.errors import PdfReadError

app = FastAPI()
@app.get("/status")
def verificar_status():
    return {"status": "online"}

@app.post("/upload")
async def receber_documento(arquivo: UploadFile = File(...)):
    limite_bytes = 10 * 1024 * 1024
    if not arquivo.filename or not arquivo.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Formato não suportado. Envie um arquivo PDF."
        )

    conteudo = bytearray() 
    while True:
     bloco = await arquivo.read(1024 * 1024)
     if not bloco:
        break
     if len(conteudo) + len(bloco) > limite_bytes:
        raise HTTPException(
        status_code=413,
        detail="Arquivo excede o limite de 10 MiB."
    )
     conteudo.extend(bloco)

    if len(conteudo) == 0:
        raise HTTPException(
        status_code=400,
        detail="O arquivo enviado está vazio."
    )

    try:
        leitor = pypdf.PdfReader(BytesIO(conteudo))
    except PdfReadError:
        raise HTTPException(
            status_code=400,
            detail="O conteúdo enviado não é um PDF válido."
        )

    texto_completo = ""

    for pagina in leitor.pages:
        texto_completo += pagina.extract_text() or ""
        texto_completo += "\n"

    return {
        "arquivo_recebido": arquivo.filename,
        "tamanho_bytes": len(conteudo),
        "paginas": len(leitor.pages),
        "texto": texto_completo
    }
