import os 
from pymongo import AsyncMongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_name = os.getenv('db_name')
mongo_url = os.getenv('mongo_url')

client = AsyncMongoClient(mongo_url)
database = client[mongo_name]