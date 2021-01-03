import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:dbAdmin@cluster0.wvxuf.mongodb.net/<dbname>?retryWrites=true&w"
                             "=majority")
db = client['EncDB']
metadata_table = db["Metadata"]
enc_table = db["Encryption"]
