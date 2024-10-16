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
  -h, --help    show this help message and exit
  --host HOST                         (0.0.0.0)
  --port PORT                         (8000)
  --mongo_db MONGO_DB, -m MONGO_DB
  --db_url DB_URL, -d DB_URL
  --data_path DATA_PATH, -p DATA_PATH (/tmp)
  --api-key API_KEY, -k API_KEY       (secret)


Start the server in simple mode

$ ./server.py
using FilePlugin: /tmp
INFO:     Started server process [674017]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


The ResourceTypes endpoint is now available at:
curl --request GET \
  --url http://localhost:8000/ResourceTypes \
  --header 'x-api-key: secret'
```

---

This repository is cloned from: [SCIM Server](https://github.com/HarryKodden/scim)
