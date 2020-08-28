from flask import Flask, jsonify
from wedding.dash import add_wedding_dash

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({'message': 'Greetings from the Backend'})


app = add_wedding_dash(app, routes_pathname_prefix='/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
