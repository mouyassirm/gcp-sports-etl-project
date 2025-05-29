import requests
import json
import filecmp
import os
from datetime import datetime
from google.cloud import storage

BASE_URL = 'https://api.football-data.org/v4/competitions'
BUCKET_NAME = 'football-data-pipeline-bucket'
DESTINATION_BLOB_NAME = 'raw/leagues.json'
LOCAL_FILE_NAME = 'leagues.json'
TEMP_EXISTING_FILE = 'existing_leagues.json'

# Appel API
response = requests.get(BASE_URL)
data = response.json()

# Sauvegarde locale
with open(LOCAL_FILE_NAME, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Upload dans Cloud Storage
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob(DESTINATION_BLOB_NAME)


# Téléchargement de l'ancien fichier pour comparaison (si existe)
need_upload = True
if blob.exists():
    print("🔍 Fichier distant existant trouvé, comparaison en cours...")
    blob.download_to_filename(TEMP_EXISTING_FILE)
    if filecmp.cmp(LOCAL_FILE_NAME, TEMP_EXISTING_FILE, shallow=False):
        print("✅ Le fichier est identique. Aucun upload nécessaire.")
        need_upload = False
    os.remove(TEMP_EXISTING_FILE)

# Upload si nécessaire
if need_upload:
    print("⬆️ Upload du nouveau fichier vers Cloud Storage...")
    blob.upload_from_filename(LOCAL_FILE_NAME)
    print(f"✅ Données uploadées dans {BUCKET_NAME}/{DESTINATION_BLOB_NAME}")