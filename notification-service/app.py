from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notifications', methods=['GET'])
def get_notifications():
    # Mock data for notifications
    notifications = [
        {"id": 1, "message": "Notification 1"},
        {"id": 2, "message": "Notification 2"}
    ]
    return jsonify(notifications)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
