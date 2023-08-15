# storage/__init__.py

from utils import mongo_db, database_url, data_path

if mongo_db:
    print(f"using MongoDB: {mongo_db}")
    from storage.plugins.mongo import MongoPlugin

    Users = MongoPlugin("Users", mongo_db)
    Groups = MongoPlugin("Groups", mongo_db)
elif database_url:
    print(f"using Database: {database_url}")
    from storage.plugins.sql import SQLPlugin

    Users = SQLPlugin('Users', database_url)
    Groups = SQLPlugin('Groups', database_url)
else:
    print(f"using FilePlugin: {data_path}")
    from storage.plugins.file import FilePlugin

    Users = FilePlugin('Users', data_path)
    Groups = FilePlugin('Groups', data_path)
