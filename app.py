# app.py
import os
from flask import Flask, send_from_directory, abort
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask App
# Serve static files from the 'static' directory relative to where app.py is
app = Flask(__name__, static_folder='static')

# Route for the homepage
@app.route('/')
def index():
    """Serves the index.html file from the current directory."""
    logging.info("Request received for / (index.html)")
    try:
        # Ensure index.html exists in the same directory as app.py
        return send_from_directory('.', 'index.html')
    except FileNotFoundError:
        logging.error("index.html not found in the current directory.")
        abort(404) # Return a 404 Not Found error

# Flask automatically handles serving files from the 'static_folder'
# when requests match the /static path.
# Example: A request to /static/css/style.css will serve static/css/style.css

# Add a simple health check endpoint (optional but good practice)
@app.route('/_healthz')
def health_check():
    return "OK", 200

if __name__ == "__main__":
    # Get port from environment variable 'PORT', default to 8080
    # Cloud Shell Web Preview typically uses 8080
    port = int(os.environ.get('PORT', 8080))

    logging.info(f"Starting Flask server on port {port}")
    # Run the app
    # Host '0.0.0.0' makes it accessible from outside the container/VM (needed for Web Preview)
    # debug=False is important for stability, especially when deploying
    app.run(debug=False, host='0.0.0.0', port=port)
