from flask import Flask, render_template, jsonify
from flask_cors import CORS  # Import CORS
import anime4aze as wit

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Routes for API endpoints
@app.route("/search-anime/<string:name>", methods=["GET"])
def search_anime(name):
    result = wit.search_anime(name)
    return jsonify(result)

@app.route("/get-episodes/<string:s_id>", methods=["GET"])
def get_episodes(s_id):
    result = wit.get_episodes(s_id)
    return jsonify(result)

@app.route("/get-episode-dl/<string:s_id>", methods=["GET"])
def get_episode_dl(s_id):
    result = wit.get_episode_dl(s_id)
    return jsonify(result)

@app.route("/latest-episodes", methods=["GET"])
def latest_episodes():
    result = wit.latest_episodes()
    return jsonify(result)

@app.route("/fetch-seasonals", methods=["GET"])
def fetch_seasonals():
    result = wit.fetch_seasonals()
    return jsonify(result)

@app.route("/get-anime-info/<string:s_id>", methods=["GET"])
def get_anime_info(s_id):
    result = wit.get_anime_info(s_id)
    return jsonify(result)

# Route for rendering HTML page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
