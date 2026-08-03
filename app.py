from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "GKE Demo",
        "message": "Application deployed successfully on Google Kubernetes Engine",
        "environment": os.getenv("ENVIRONMENT", "Development"),
        "version": "1.0"
    }

@app.route("/health")
def health():
    return {"status": "UP"}

@app.route("/employees")
def employees():
    return [
        {"id": 101, "name": "John"},
        {"id": 102, "name": "David"},
        {"id": 103, "name": "Sara"}
    ]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
