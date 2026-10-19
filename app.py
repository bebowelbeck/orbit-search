
from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/fetch")
def fetch_page():
    url = "https://example.com"

    try:
        response = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "OrbitTest/1.0"}
        )

        return jsonify({
            "status_code": response.status_code,
            "html": response.text
        })

    except requests.RequestException:
        return jsonify({
            "error": "Could not fetch the test webpage"
        }), 502

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
