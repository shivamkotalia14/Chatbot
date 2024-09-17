from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    text = request.form['text']
    video = request.files['video']
    # Save video to a folder
    video.save(f'./uploads/{video.filename}')
    response_message = f"Received text: {text}. Video: {video.filename}" if video else f"Received text: {text}. No video uploaded."
    
    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)
