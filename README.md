# SCIM-server

A simple SCIM server for testing/monitoring purposes

## Installation

```
$ git clone https://github.com/SURFscz/SCIM-server.git
$ cd SCIM-server
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

```
usage: server.py [-h] [--host HOST] [--port PORT] [--mongo_db MONGO_DB] [--db_url DB_URL] [--data_path DATA_PATH] [--api-key API_KEY]

SCIM Test server.

options:
  -h, --help            show this help message and exit
  --host HOST
  --port PORT
  --mongo_db MONGO_DB, -m MONGO_DB
  --db_url DB_URL, -d DB_URL
  --data_path DATA_PATH, -p DATA_PATH
  --api-key API_KEY, -k API_KEY
```

---

This repository is cloned from: [SCIM Server](https://github.com/HarryKodden/scim)
