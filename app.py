from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os
import socket

app = Flask(__name__)

metrics = PrometheusMetrics(app)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return jsonify({
        "application": "devops-portfolio-app",
        "version": APP_VERSION,
        "hostname": socket.gethostname(),
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/products")
def products():
    return jsonify({
        "products": [
            {
                "id": 1,
                "name": "Laptop",
                "price": 75000
            },
            {
                "id": 2,
                "name": "Monitor",
                "price": 25000
            },
            {
                "id": 3,
                "name": "Keyboard",
                "price": 3000
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)