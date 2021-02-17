import pymongo

client = pymongo.MongoClient("mongoURI")
db = client['EncDB']

metadata_table = db["Metadata"]
enc_table = db["Encryption"]
