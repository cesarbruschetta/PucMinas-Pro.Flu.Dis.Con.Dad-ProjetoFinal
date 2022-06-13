from typing import Any, Dict

import uvicorn
from fastapi import FastAPI

from mongo_db import consulta_recomendacoes, inicia_conexao


app = FastAPI()
conexao = inicia_conexao()


@app.get("/rec/v1")
def rota_padrao() -> Dict[str, str]:
    return {"Rota padrão": "Você acessou a rota default"}


@app.get("/rec/v2/{usuario}")
def consulta_rec(usuario: int) -> Dict[str, Any]:
    return {
        "usuario": usuario,
        "resultado_recs": consulta_recomendacoes(usuario, conexao),
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
