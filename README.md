## Progeto Final 

Projeto final da materia de _Processamento de Fluxo discreto e constantes de dados_ do curso de Pos-graduação da PUC-MG no ano de 2022


## Roteiro do projeto:

Vamos gerar recomendações utilizando a MLlib do Spark, em específico o modelo ALS. Essas recomendações serão armazenadas no MongoDB, executado localmente. Os alunos que preferirem podem alterar a prática para utilizar imagens docker.

Uma vez armazenadas as recomendações será criada uma API com a biblioteca FastAPI, para retornar solicitações de recomendações com base no ID do usuário.

## Etapas a serem desenvolvidas pelo aluno:

Com base na atividade de Spark Streaming, crie uma aplicação Spark que se conecta em um tópico do Kafka, onde serão publicadas mensagens contendo o ID do usuário e consulte utilizando a biblioteca do Mongo Spark Connector ou similar, as recomendações para o usuário enviado em um tópico a ser definido pelo aluno. Essa aplicação irá substituir a API.
 Observação 1: as bibliotecas sugeridas foram apresentadas previamente na prática referente ao Spark Streaming, e podem ser utilizadas como referência.
Para a execução dessa atividade utilizaremos o modelo de recomendação feito em aula, com utilização do Apache Spark, o banco de dados MongoDB e um exemplo de API feito utilizando FastAPI. Todo esse procedimento será apresentado em aula.