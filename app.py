from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Alex's Backend API!"})

@app.route("/joke")
def joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()

    return jsonify({
        "setup": data["setup"],
        "punchline": data["punchline"]
    })

@app.route("/github/<username>")
def github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    data = response.json()

    return jsonify({
        "username": data["login"],
        "repos": data["public_repos"],
        "followers": data["followers"],
        "following": data["following"]
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)