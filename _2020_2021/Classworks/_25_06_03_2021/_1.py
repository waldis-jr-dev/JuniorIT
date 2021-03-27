from flask import Flask, redirect
import string

alpha = string.ascii_letters

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


@app.route('/', methods=['GET'])
def index():
    return 'Encode / Decode'


@app.route('/encode/<context>/<key>', methods=['GET'])
def encode(context, key):
    resp = ''
    for letter in context:
        resp += alpha[(alpha.index(letter) + int(key)) % len(alpha)]
    return resp


@app.route('/decode/<encoded>/<key>', methods=['GET'])
def decode(encoded, key):
    resp = ''
    for letter in encoded:
        resp += alpha[(alpha.index(letter) - int(key)) % len(alpha)]
    return resp


if __name__ == '__main__':
    app.run(debug=True, port=5001)


