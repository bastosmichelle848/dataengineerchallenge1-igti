# 1º Data engineering's challenge

1. Ingest the RAIS 2020 PUBLIC LINKS data into AWS S3 or other cloud storage of your choice. Data is available at: http://pdet.mte.gov.br/microdados-rais-e-caged (we will not work with data from ESTABLISHMENTS). The method of ingestion is free. Data must be ingested in the raw zone or raw zone or bronze zone of your Data Lake;

>> I chose to upload the files by python with the script at interact_s3.py (I didn't upload the entire dataset, I chose to upload one by one).

2. Treat the RAIS 2020 dataset and follow the steps below (when in doubt, consult the code at: https://github.com/neylsoncrepalde/igti_edc_mod1_desafio_final_rais/blob/main/etl/emr-rais.ipynb and remember that it was thought to run in EMR):
The. Modify the column names, replace spaces with “_”, remove accents and put all lowercase letters;
B. Build the column “uf” with the following command: rais = rais.withColumn("uf", f.col("municipio").cast('string').substr(1,2).cast('int') )
ç. Modify the pay columns to be of type double.

3. Transform the data into parquet format and write it to the staging zone or silver zone of your Data Lake.

4. Integrate with some Data Lake engine. In the case of AWS, you must:
The. Configure a Crawler for the folder where the staging files are deposited;
B. Validate availability in Athena.

5. If you want to use Google, make the data available for a query using Big Query. If you use another cloud, the choice of the Data Lake engine is free.

6. Use the Big Data tool or the Data Lake engine (or BigQuery, if you choose to work with Google Cloud) to investigate the data and answer the challenge questions.

7. When the architecture design is ready, create a repository on Github (or Gitlab, Bitbucket, or another of your choice) and place the IaC code for the infrastructure deployment. No features should be manually deployed.
