

from pymongo.mongo_client import MongoClient
import pandas as pd
import json

##URL
url="mongodb+srv://anujmishra77386:Anuj12345@cluster0.uamtx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
##create a new client and connect a server
client=MongoClient(url)


##create a database name and collection name
DATABASE_NAME="ANUJ_project"
COLLECTION_NAME="Wafer_fault_sensor "

df=pd.read_csv("C:\Users\shiva\Downloads\Sensor_project\notebooks\wafer_23012020_041211.csv")


df.head()

df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

