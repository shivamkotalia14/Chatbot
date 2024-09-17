from flask import Flask, request, jsonify
from flask_cors import CORS
from src.classifier import *
from src.bert import *
from src.landmarker import *
from src.llm import LLM
from src.recognition import Recognition
from src.store import Store
from src.utils import *

app = Flask(__name__)
CORS(app)

@app.route('/uploads', methods=['POST'])
def upload():
    text = "hi"
    video = "data.mp4"
    # Save video to a folder
    video.save(f'./uploads/{video.filename}')
    response_message = f"Received text: {text}. Video: {video.filename}" if video else f"Received text: {text}. No video uploaded."
    llm = LLM()
    recognition = Recognition()
    camera = cv2.VideoCapture("C:/Users/USER/Chatbot/chatbot-backend/data.mp4")
    print(camera)
    query_from_asl_recogniser = recognize(camera, recognition)
    if query_from_asl_recogniser is not None:
        final_query = llm.gloss(query_from_asl_recogniser)
    else:
        print("No output from recognition.")
    return jsonify({'message': final_query})

if __name__ == '__main__':
    app.run(debug=True)
