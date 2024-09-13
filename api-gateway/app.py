from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "API Gateway is running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
