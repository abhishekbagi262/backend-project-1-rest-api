from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to my REST API!",
        "status": "success"
    })

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello from my Backend API!",
        "status": "success"
    })

@app.route("/users",methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "course" not in data:
        return jsonify({
            "message": "Name and course are required!",
            "status": "Error"
        }), 400

    return jsonify({
        "message": "user created successfully!",
        "status": "success",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)