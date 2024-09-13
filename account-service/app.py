from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/accounts', methods=['GET'])
def get_accounts():
    # Mock data for accounts
    accounts = [
        {"id": 1, "name": "Account 1"},
        {"id": 2, "name": "Account 2"}
    ]
    return jsonify(accounts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
