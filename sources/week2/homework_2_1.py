import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.students
grades = db.grades

iter = grades.find({'score': {'$gte': 65}}).sort([('score', 1)]).limit(1)

sanity = 0
for doc in iter:
    print doc
