from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/trades', methods=['GET'])
def get_trades():
    # Mock data for trades
    trades = [
        {"id": 1, "type": "buy", "amount": 100},
        {"id": 2, "type": "sell", "amount": 50}
    ]
    return jsonify(trades)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
