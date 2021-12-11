from flask import Flask, jsonify, request, abort

app = Flask(__name__)

CARD_BALANCE = 20


@app.route('/inspect')
def inspect():
    return jsonify({
        "available": 1
    })


@app.route('/request_payment', methods=['POST'])
def request_payment():
    data = request.get_json(force=True)

    cart_id = data.get('cart_id')
    amount = data.get('amount')

    if cart_id is None:
        abort(400, {'cart_id': "This field is required"})

    if amount is None:
        abort(400, {'amount': "This field is required"})

    if not isinstance(cart_id, int) or not isinstance(amount, int):
        abort(400, {'type': "The fields should be integers."})

    if amount >= CARD_BALANCE:
        abort(400, {
            'cart_id': cart_id,
            'payment_status': "failed"
        })

    return jsonify({
        'cart_id': cart_id,
        'payment_status': "success"
    })


if __name__ == '__main__':
    app.run()
