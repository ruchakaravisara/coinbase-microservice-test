from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/wallets', methods=['GET'])
def get_wallets():
    # Mock data for wallets
    wallets = [
        {"id": 1, "balance": 1000},
        {"id": 2, "balance": 500}
    ]
    return jsonify(wallets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
