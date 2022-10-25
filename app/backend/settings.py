# third party
from decouple import config, Csv

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())
ALLOWED_ORIGINS = config("ALLOWED_ORIGINS", default="", cast=Csv())

MONGODB_HOST = config("MONGO_DB_HOST")
MONGODB_NAME = config("MONGO_DATABASE")
MONGODB_USER = config("MONGO_ROOT_USERNAME")
MONGODB_PASS = config("MONGO_ROOT_PASSWORD")
MONGODB_URL = f"mongodb://{MONGODB_HOST}/{MONGODB_NAME}"
