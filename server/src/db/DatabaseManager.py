import pymongo

from env_vars import (
    MONGODB_CONNECTION_STRING,
    MONGODB_DB_NAME
)

class DatabaseManager:
    def __init__(self) -> None:
        client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
        self.db = client.get_database(MONGODB_DB_NAME)
