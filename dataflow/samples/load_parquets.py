import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import storage
import os
import json
from datetime import datetime

# GCS config
BUCKET_NAME = 'football-data-pipeline-bucket'
RAW_BLOB_NAME = 'raw/leagues.json'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
CLEANED_JSON_NAME = f'processed/leagues_cleaned_{timestamp}.json'
PARQUET_NAME = f'parquet/leagues_cleaned_{timestamp}.parquet'

# Init GCS client
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

# Téléchargement du fichier JSON brut
raw_blob = bucket.blob(RAW_BLOB_NAME)
raw_blob.download_to_filename('raw.json')

# Chargement JSON
with open('raw.json', 'r') as f:
    data = json.load(f)

df = pd.json_normalize(data['competitions'])

# Table des continents
df_continents = df[['area.id', 'area.name', 'area.code']].drop_duplicates().rename(columns={
    'area.id': 'area_id',
    'area.name': 'area_name',
    'area.code': 'area_code'
})

# Table des compétitions
df_competitions = df[['id', 'name', 'type', 'code', 'plan', 'area.id', 'currentSeason.id', 'numberOfAvailableSeasons']].rename(columns={
    'area.id': 'area_id',
    'currentSeason.id': 'currentSeason_id'
})

# Table des saisons (à partir de currentSeason)
df_saisons = df[['currentSeason.id', 'currentSeason.startDate', 'currentSeason.endDate', 'currentSeason.currentMatchday', 'currentSeason.winner', 'id']].rename(columns={
    'currentSeason.id': 'id',
    'currentSeason.startDate': 'start_date',
    'currentSeason.endDate': 'end_date',
    'currentSeason.currentMatchday': 'current_matchday',
    'currentSeason.winner': 'winner',
    'id': 'competition_id'
})

# Sauvegarde Parquet
df_continents.to_parquet('continents.parquet')
df_competitions.to_parquet('competitions.parquet')
df_saisons.to_parquet('saisons.parquet')

# Upload vers GCS
bucket.blob('parquet/continents.parquet').upload_from_filename('continents.parquet')
bucket.blob('parquet/competitions.parquet').upload_from_filename('competitions.parquet')
bucket.blob('parquet/saisons.parquet').upload_from_filename('saisons.parquet')
