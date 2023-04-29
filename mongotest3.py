import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://princefrancis64:Oejb2e2l74Gz4NAK@cluster0.o5qm0dq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


d = {
   "name":"prince1",
   "email":"prince.francis64@gmail.com",
   "surname":"francis"
    }

database = client['practice']
collection = database['mongodb']
collection.insert_one(d)
#record = collection.find()
#data = collection.find({'companyName':'iNeuron'})
#d= collection.find({'status':'A'})
#d=collection.find({'status':{'$in':['A','P']}})
#d= collection.find({'status':{'$gt':'C'}})
#d= collection.find({'qty':{'$gte':75}})
#d= collection.find({'item':'sketch pad', 'qty':{'$gte':95}})
#d= collection.find({'item':'sketch pad', 'qty':{'$gte':75}})
#d =collection.find({'$or':[{'item':'sketchpad'}, {'qty':{'$gte':75}}]})
#collection.update_one({'item':'canvas'}, {'$set':{'item':'prince'}})
collection.delete_one({'item':'prince'})
for i in d:
    print(i)