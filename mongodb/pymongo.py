from pymongo import MongoClient


#connection to Database
connection = MongoClient(port=27017)
db = connection.mydb

#handle to users Collection
users = db.users

users_data = [
{
    'name' : 'Sarah',
    'lastname' : 'Ahmadi',
    'age' : '23'
},
{
    'name' : 'Ahmad',
    'lastname' : 'Minaee',
    'age' : '31'
},
{
    'name' : 'Ali',
    'lastname' : 'azimi',
    'age' : '29'
},
{
    'name' : 'Roya',
    'lastname' : 'Moradi',
    'age' : '25'
},
{
    'name' : 'Mehdi',
    'lastname' : 'Mohammadi',
    'age' : '23'
}
]

result = users.insert_many(users_data)


# Querying for More Than One Document

# for user in users.find():
#     print(user)

for user in users.find({'age' : '23'}):
    print(user)

# Counting
count = users.count_documents({})
print('Count value is: ', count)
