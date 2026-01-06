from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/api/status")
def status():
    return jsonify(service="DeployBoard Backend", status="running")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
