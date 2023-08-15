# __init__.py
import os
import argparse

parser = argparse.ArgumentParser(description='SCIM Test server.')
parser.add_argument('--host', default='0.0.0.0')
parser.add_argument('--port', default=8000, type=int)
parser.add_argument('--mongo_db', '-m')
parser.add_argument('--db_url', '-d')
parser.add_argument('--data_path', '-p')
parser.add_argument('--api-key', '-k')
args = parser.parse_args()

# Server options
host = args.host
port = args.port

# Backend option: Mongo DB
mongo_db = args.mongo_db or os.environ.get("MONGO_DB", None)

# Backend option: SQL Databases
database_url = args.db_url or os.environ.get("DATABASE_URL", None)

# Backend option: File
data_path = args.data_path or os.environ.get("DATA_PATH", "/tmp")

# API Key
api_key = args.api_key or os.environ.get("API_KEY", "secret")
