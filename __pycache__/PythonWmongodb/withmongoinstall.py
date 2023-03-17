import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
item_1={
    id:"12445abms",
    "name":"jay",
    "age":23
}
item_2={
    id:"56243abms",
    "name":"jaymit",
    "age":36
}
mydb.insert_many([item_1,item_2])
mydb.find()