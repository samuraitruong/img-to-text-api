from flask import Flask, request, jsonify
from image_to_text import extract_text_from_image
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='api.log', level=logging.INFO)

@app.before_request
def log_request_info():
    logging.info(f'Request: {request.method} {request.url}')

@app.after_request
def log_response_info(response):
    logging.info(f'Response: {response.status_code}')
    return response



@app.route('/', methods=['GET'])
def hello():
    return jsonify("OK")

@app.route('/extract_text', methods=['POST'])
def upload_image():
    
    # Check if a file was provided in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']
    image_binary = file.read()

    # Extract text from the image
    extracted_text = extract_text_from_image(image_binary)

    return jsonify({'text': extracted_text})

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    