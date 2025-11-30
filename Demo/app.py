from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy device list (replace with Netmiko/NX-API later)
devices = [
    {"name": "Nexus1", "model": "Nexus 9300", "serial": "ABC12345", "version": "9.3(5)"},
    {"name": "Nexus2", "model": "Nexus 9500", "serial": "XYZ67890", "version": "10.2(1)"},
    {"name": "ACI-Leaf1", "model": "ACI Leaf", "serial": "LEAF111", "version": "5.2(3)"},
]

@app.route("/")
def index():
    return render_template("index.html", devices=devices)

@app.route("/inventory")
def inventory():
    model_filter = request.args.get("model", "all")
    if model_filter == "all":
        results = devices
    else:
        results = [d for d in devices if d["model"] == model_filter]
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)