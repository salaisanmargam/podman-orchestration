from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/div", methods=["POST"])
def div():
    data = request.json
    a = float(data["a"])
    b = float(data["b"])
    if b == 0:
        return jsonify({"error": "Division by 0"})
    return jsonify({"result": a / b})

app.run(host="0.0.0.0", port=5000)
