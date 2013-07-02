import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.school
students = db.students

it = students.find()
for student in it:
	minhomework = min(s['score'] for s in student['scores'] if s['type'] == 'homework')
	res = students.update({'_id' : student['_id']}, { '$pull': { 'scores' : { 'type' : 'homework', 'score': minhomework } }})
	print res

