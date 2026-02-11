from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/mul", methods=["POST"])
def mul():
    data = request.json
    a = float(data["a"])
    b = float(data["b"])
    return jsonify({"result": a * b})

app.run(host="0.0.0.0", port=5000)
