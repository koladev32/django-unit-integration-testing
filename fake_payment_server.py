from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/inspect')
def inspect():
    return jsonify({
        "available": 1
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)