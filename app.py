import json
from flask import Flask, render_template, jsonify
import anime4aze as wit 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search-anime/<string:name>", methods=["GET"])
def search_anime_api(name):
    try:
        result = wit.search_anime(name)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)