from pymongo import MongoClient
#Create
client = MongoClient('localhost',27017)
db=client.dbsparta
# db.users.insert_one({'name':'유현다','age':22})
# db.users.insert_one({'name':'이지은','age':25})
# db.users.insert_one({'name':'김나영','age':29})

#Read
all_users = list(db.users.find({}))
print(all_users)

print(all_users[0]['name'])
user = db.users.find_one({'name':'유현다'})
print(user)

#Update
#db.users.update_one({'name':'이지은'},{'$set':{'age':30}})
db.users.update_many({'name':'이지은'},{'$set':{'age':95}})
all_users = list(db.users.find({}))
print(all_users)

#Delete
db.users.delete_one(all_users[2])
all_users = list(db.users.find({}))
print(all_users)

db.users.delete_many({'name':'이지은'})
all_users = list(db.users.find({}))
print(all_users)