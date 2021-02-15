from flask import Flask, request, jsonify
import configparser
from utils import *


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/api/getArtifact", methods=["GET", "POST"])
def getArtifact():
    access_token = "XXXXXXXXXXXXXXXXXX"
    if request.method == 'POST':
        img = request.form.get('image')
        try:
            artifact = get_stat(img, access_token)
            return jsonify(artifact.__str__())
        except:
            return "false", 500


app.run(host='0.0.0.0', port=5000)
