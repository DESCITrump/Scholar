from flask import jsonify, request
from app import db
from app.models import Scholarship
from . import api
from flask_jwt_extended import jwt_required

@api.route('/scholarships', methods=['POST'])
@jwt_required()
def add_scholarship():
    data = request.get_json()
    new_scholarship = Scholarship(name=data['name'], description=data['description'], deadline=data['deadline'], amount=data['amount'])
    db.session.add(new_scholarship)
    db.session.commit()
    return jsonify({'message': 'Scholarship added successfully'}), 201

@api.route('/scholarships', methods=['GET'])
@jwt_required()
def get_scholarships():
    scholarships = Scholarship.query.all()
    return jsonify([{'id': sch.id, 'name': sch.name, 'deadline': sch.deadline, 'amount': sch.amount} for sch in scholarships])