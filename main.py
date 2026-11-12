import pypdf
import json
from fastapi import FastAPI

app = FastAPI()
@app.get("/status")
def verificar_status():
    return {"status": "online"}

from pathlib import Path
pasta_projeto = Path(__file__).resolve().parent
print(pasta_projeto)

caminho_pdf = pasta_projeto / "documentos" / "NF_Ficticia_Teste_Document_Intelligence.pdf"

print(caminho_pdf.exists())

def extrair_documento():
    leitor = pypdf.PdfReader(caminho_pdf)
    print(len(leitor.pages))

    texto_completo = ""

    for pagina in leitor.pages:
        texto_completo += pagina.extract_text()

    print(texto_completo)

    resultado = {
        "arquivo": caminho_pdf.name,
        "paginas": len(leitor.pages),
        "texto": texto_completo
    }

    return resultado

@app.get("/documento")
def consultar_documento():
    return extrair_documento()