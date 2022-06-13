from typing import Any, Dict

from pymongo import MongoClient
from pymongo.collection import Collection


def inicia_conexao() -> Collection:
    client = MongoClient(
        'mongodb://root:root@127.0.0.1:27017'
    )
    db = client['puc']
    col = db.recomendacoes
    return col


def consulta_recomendacoes(
    usuario: int, conexao: Collection
) -> Dict[str, Any]:

    recomendacoes = list(conexao.find({"userId": usuario}))
    list_rec = []
    for rec in recomendacoes:
        list_rec.append((rec['movieId'], rec['rating']))

    return {'Recomendações': list_rec}
