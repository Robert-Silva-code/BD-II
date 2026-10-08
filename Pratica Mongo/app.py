#robertvinicius_db_user
#bOB3roQmNSjv1kfj


from pymongo import MongoClient
uri = "mongodb+srv://robertvinicius_db_user:bOB3roQmNSjv1kfj@cluster0.t6y1ytg.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)