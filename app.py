from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

@app.route('/about')
def about():
    return jsonify({"version": "1.0", "author": "Yagmur Ozden"}), 200

if __name__ == '__main__':
    app.run(debug=True)
    
    
# First, you need to install Flask using pip:

# pip install Flask

# To run the python script
# python app.py
# This script will start a server on your localhost. You can access the following URLs in your browser or using a tool like Postman to test your RESTful service:

# http://localhost:5000/ : returns a JSON message 
# http://localhost:5000/about : returns a JSON object with version and author information

# The server runs in debug mode, which means it will automatically reload when you make changes to the script.
