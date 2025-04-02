from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

# Load responses from the JSON file
with open("responses.json", "r") as f:
    data = json.load(f)
    responses = data["responses"]

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.json.get('text', '')
    # Pick a random response from the JSON file
    reply = random.choice(responses)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
