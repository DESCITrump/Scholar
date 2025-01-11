from app import create_app
from flask import jsonify, request
app = create_app()

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json.get('message', '')
    response = "This is a placeholder for AI response"
    return jsonify({'response': response})