"""
    Script para a generação e construção das recomendações de Filmes para os usuarios
"""

from pathlib import Path

import findspark
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import DataFrame, Row, SparkSession


findspark.init()
findspark.find()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def read_dataset(spark: SparkSession) -> DataFrame:
    lines = spark.read.text(
        str(BASE_DIR.joinpath("data/sample_movielens_ratings.txt"))
    ).rdd
    parts = lines.map(lambda row: row.value.split("::"))
    ratingsRDD = parts.map(
        lambda p: Row(
            userId=int(p[0]),
            movieId=int(p[1]),
            rating=float(p[2]),
            timestamp=int(p[3]),
        )
    )
    return spark.createDataFrame(ratingsRDD.collect())


def build_model(df_ratings: DataFrame) -> ALS:

    (training, test) = df_ratings.randomSplit([0.8, 0.2])

    als = ALS(
        maxIter=5,
        regParam=0.01,
        userCol="userId",
        itemCol="movieId",
        ratingCol="rating",
        coldStartStrategy="drop",
    )
    model = als.fit(training)

    predictions = model.transform(test)
    evaluator = RegressionEvaluator(
        metricName="rmse", labelCol="rating", predictionCol="prediction"
    )
    rmse = evaluator.evaluate(predictions)
    print("Root-mean-square error = " + str(rmse))

    return model


def run() -> None:
    spark = (
        SparkSession.builder.appName("BuildModelInALS")
        .config(
            "spark.mongodb.input.uri",
            "mongodb://root:root@127.0.0.1:27017/puc",
        )
        .config(
            "spark.mongodb.output.uri",
            "mongodb://root:root@127.0.0.1:27017/puc",
        )
        .config(
            'spark.jars.packages',
            'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1',
        )
        .getOrCreate()
    )
    print('\tCriando sessão do spark...')

    dataset = read_dataset(spark)
    print('\tLendo o dataset dos filmes...')

    model = build_model(dataset)
    print('\tConstruindo o model ALS...')

    userRecs = model.recommendForAllUsers(50)

    save_data = userRecs.select(
        userRecs["userId"],
        userRecs["recommendations"]["movieId"].alias("movieId"),
        userRecs["recommendations"]["rating"].alias("rating"),
    )

    save_data.write.format("com.mongodb.spark.sql.DefaultSource").option(
        "uri",
        "mongodb://root:root@localhost:27017/puc.recomendacoes?authSource=admin",
    ).mode("append").save()

    print('\tSalvando os dados no MongoDB...')


if __name__ == "__main__":
    print('Executando processamento das recomendações...')
    run()
