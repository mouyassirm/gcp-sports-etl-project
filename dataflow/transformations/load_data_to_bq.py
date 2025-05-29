from google.cloud import bigquery

# Config
project_id = "football-data-pipeline-461212"
dataset_id = "football"
bucket = "football-data-pipeline-bucket"

# Nom des fichiers Parquet déjà uploadés
parquets = {
    "continents": f"gs://{bucket}/parquet/continents.parquet",
    "competitions": f"gs://{bucket}/parquet/competitions.parquet",
    "saisons": f"gs://{bucket}/parquet/saisons.parquet",
}

client = bigquery.Client(project=project_id)

for table, uri in parquets.items():
    table_id = f"{project_id}.{dataset_id}.{table}"
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE  # remplace les données existantes
    )
    print(f"⏳ Chargement de {uri} vers {table_id}...")
    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()  # Bloque jusqu'à la fin du job
    print(f"✅ Table {table} chargée avec succès.")
