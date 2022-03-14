from crypt import methods
from flask import Flask

app = Flask(__name__)

srotes = [
    {
        'name': 'Store 1', 
        'items': [
            { 'name': 'My Item', 'price': 15.99 } ,
        ],
    }
]

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET  /store/<name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET  /store
@app.route('/store')
def get_stores():
    pass

# POST /store/<name>/<item> {name, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item():
    pass

# GET  /store/<name>/<item>
@app.route('/store/<string:name>/item')
def get_store_items():
    pass

app.run(port=4258)