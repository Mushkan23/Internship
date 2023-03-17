show dbs
show collections
db.sub.find()
db.sub.aggregate([{$group: {"_id":"$_id","name":{"$first":"$name"}}}])
