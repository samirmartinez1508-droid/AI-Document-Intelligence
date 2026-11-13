# AI Document Intelligence

API de extração de texto de documentos PDF, desenvolvida com Python e FastAPI, com integração planejada ao n8n para automação e processamento inteligente de documentos.

## Status

Em desenvolvimento.


## Instalação

Clone o repositório e acesse a pasta do projeto.

```bash
git clone https://github.com/samirmartinez1508-droid/AI-Document-Intelligence.git
cd AI-Document-Intelligence
```

### macOS / Linux

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

Crie o ambiente virtual:

```powershell
py -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

## Executando a API

Com o ambiente virtual ativado, inicie o servidor:

```bash
python -m uvicorn main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

### Endpoints

- `GET /status` — verifica se a API está online.
- `POST /upload` — recebe um PDF e retorna o nome, o tamanho, a quantidade de páginas e o texto extraído.
