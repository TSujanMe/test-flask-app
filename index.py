
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def fetchlove():
    return jsonify({"message": "Immense love for her"})

@app.route('/', methods=['POST'])
def home():
    body = request.files.get("fike")
    return jsonify({"file": "test"})

@app.route('/fetch_google', methods=['GET'])
def fetch_googlee():
    # Replace 'https://www.google.com' with the desired URL
    url = 'https://www.google.com'
    
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Return the response content as JSON
    return jsonify(content=response.text)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
