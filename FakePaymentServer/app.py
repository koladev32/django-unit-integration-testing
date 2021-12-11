from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def inspect():
    return jsonify({
        "available": 1
    })


if __name__ == '__main__':
    app.run()
