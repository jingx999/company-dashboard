from flask import Flask, jsonify
from flask_cors import CORS

from faker import Faker

import random

app = Flask(__name__)
CORS(app)
fake = Faker()


@app.route('/api/hello')
def hello():
    return jsonify(message="hello from flask......")


@app.route('/api/sales_data')
def get_data():
    data = [{
        'date': fake.date_this_year().strftime("%Y-%m-%d"),
        'sales': random.randint(100, 200)
    } for _ in range(30)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )