
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Replace this with your exact student registration number
REGISTRATION_NUMBER = "FA23-BDS-034"

random.seed(REGISTRATION_NUMBER)

a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)


@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])

        y = a1*x1 + a2*x2 + a3*x3 + b

        return jsonify({
            "registration number": FA23-BDS-034,
            "prediction": round(y, 2)
        })

    except (KeyError, ValueError):
        return jsonify({
            "error": "Please provide numeric x1, x2 and x3"
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
