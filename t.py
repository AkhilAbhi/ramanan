from config import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
uri = "mongodb+srv://akhil:BveFI008IWZlYLPg@ramanan.rx6xwkn.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
#try:
    #client.admin.command('ping')
    #print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
    #print(e)


#########
#url ="mongodb+srv://akhil:BveFI008IWZlYLPg@ramanan.rx6xwkn.mongodb.net/?retryWrites=true&w=majority"

#clu = MongoClient(url)
db = client['ramanan']
col = db['ramanan']
def uploadData():
  name="chel"
  url="chekkkk"
  print("uplodinggg")
  data = {"name":name,"url":url}
  col.insert_one(data)
  print("doneee")
  #await app.send_message(message.from_user.id,"uploded to data base")
uploadData()