import pymongo
client=pymongo.MongoClient("localhost",27017)
db=client.publications
#collec=db.zikaVirus2


print("Generating Collection zikaVirus2")
pipeline=[db.zikaVirus2.aggregate([
{"$match":{"fullText":{"$exists": "true"}}},
{"$out": "pub_fulltext_1"}
])]

print("Generating Collection hivNef")
pipeline=[db.hivNef.aggregate([
{"$match":{"fullText":{"$exists": "true"}}},
{"$out": "pub_fulltext_2"}
])]

#db.collec.aggregate(pipeline)

#print(type(pipeline.batch_size))
