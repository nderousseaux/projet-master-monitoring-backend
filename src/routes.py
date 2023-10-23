from flask import jsonify

from main import app

@app.route("/", methods=["GET"])
def index():
	return jsonify({'message': 'Hello world!'}), 200