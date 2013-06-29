import bottle
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.m101

@bottle.route('/')
def home():
    return bottle.template('views/index.html')

@bottle.route('/hw1_1')
def homework1_1():
    model = db.hw1.find_one()
    return bottle.template('views/homework1/hw1-1.html', answer=model['answer'], question=model['question'])

@bottle.route('/hw1_2')
def homework1_2():

    collection = db.funnynumbers
    magic = 0

    numbers = collection.find()
    for item in numbers:
        if item['value'] % 3 == 0:
            magic = magic + item['value']

    return bottle.template('views/homework1/hw1-2.html', result=magic)

@bottle.route('/hw1_3/<n>')
def homework1_3(n):

    collection = db.funnynumbers
    items = collection.find({},limit=1, skip=int(n)).sort('value', direction=1)
    result = ''
    for item in items:
        result = result + str(int(item['value'])) + "\n"

    return bottle.template('views/homework1/hw1-3.html', result=result, n=n)


@bottle.route("/css/<file:path>")
def serve_static_style(file):
    return bottle.static_file(file, "css/")

@bottle.route("/js/<file:path>")
def serve_static_script(file):
    return bottle.static_file(file, "js/")

bottle.run(host='localhost', port=8080)