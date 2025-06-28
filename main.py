from flask import Flask, request, jsonify
import time
import base64
import re

app = Flask(__name__)

# /data - Base64 encode string
@app.route('/data', methods=['POST'])
def encode_data():
    data = request.get_json(force=True)
    string = data.get("data", "")
    encoded = base64.b64encode(string.encode()).decode()
    return jsonify({"result": encoded})

# /zap - Remove all digits from input
@app.route('/zap', methods=['POST'])
def zap_digits():
    data = request.get_json(force=True)
    string = data.get("data", "")
    cleaned = re.sub(r'\d', '', string)
    return jsonify({"result": cleaned})

# /alpha - Check if input contains any letter
@app.route('/alpha', methods=['POST'])
def contains_alpha():
    data = request.get_json(force=True)
    string = data.get("data", "")
    has_alpha = bool(re.search(r'[a-zA-Z]', string))
    return jsonify({"result": has_alpha})

@app.post("/fizzbuzz")
def fizzbuzz():
    return jsonify({ "result": False })

# /time - Countdown to fixed timestamp (Oct 6, 2093)
@app.route('/time', methods=['GET'])
def time_left():
    target_timestamp = 4071760602  # Fixed future timestamp
    remaining = int(target_timestamp - time.time())
    return jsonify({"result": max(0, remaining)})

@app.post("/glitch")
def glitch_string():
    data = request.get_json(force=True)
    s = data.get("data", "")
    specials = ''.join([c for c in s if not c.isalnum()])
    rest = ''.join([c for c in s if c.isalnum()])[::-1]
    return jsonify({ "result": specials + rest })

if __name__ == '__main__':
    app.run(debug=True)
