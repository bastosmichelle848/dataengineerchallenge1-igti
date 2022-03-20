import boto3
import pandas as pd

#Criar um cliente para interagir com s3

s3_client = boto3.client('s3')

s3_client.upload_file("C:/Users/Michelle/Documents/igti-desafio1/data/rais_2020/RAIS_VINC_PUB_NORDESTE.7z",

"raw-data-igti",

"data/rais_2021/RAIS_VINC_PUB_NORDESTE.7z")

