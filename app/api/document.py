from flask import jsonify, request
from app import db
from app.models import Document
from . import api
from flask_jwt_extended import jwt_required

@api.route('/documents', methods=['POST'])
@jwt_required()
def add_document():
    data = request.get_json()
    new_document = Document(title=data['title'], content=data['content'])
    db.session.add(new_document)
    db.session.commit()
    return jsonify({'message': 'Document added successfully'}), 201

@api.route('/documents', methods=['GET'])
@jwt_required()
def get_documents():
    documents = Document.query.all()
    return jsonify([{'id': doc.id, 'title': doc.title, 'upload_date': doc.upload_date} for doc in documents])