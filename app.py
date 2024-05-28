from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"id": 1})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)