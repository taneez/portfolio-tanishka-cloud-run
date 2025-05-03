# app.py
import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static') # Point to the static folder

# Route for the homepage (index.html)
@app.route('/')
def index():
    # Serve index.html from the root directory where app.py is located
    return send_from_directory('.', 'index.html')

# Flask automatically handles serving files from the 'static_folder'
# specified above when requests come in for /static/*
# So, no explicit route needed for /static/css/style.css or /static/js/game.js

if __name__ == "__main__":
    # Get port from environment variable or default to 8080
    port = int(os.environ.get('PORT', 8080))
    # Run the app, listening on all available interfaces
    app.run(debug=False, host='0.0.0.0', port=port)