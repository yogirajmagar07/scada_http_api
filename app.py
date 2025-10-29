from flask import Flask, request, jsonify
from database import insert_data

app = Flask(__name__)

@app.route('/API/', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()  # receive JSON payload
        print("✅ Received data:", data)

        # simulate saving to MySQL
        insert_data(data)

        return jsonify({"status": "success", "received": data}), 200
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    # run locally on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
