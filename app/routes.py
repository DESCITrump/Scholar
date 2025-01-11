from flask import Blueprint, render_template, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Document, Scholarship

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/documents')
@jwt_required()
def documents():
    docs = Document.query.all()
    return render_template('documents.html', documents=docs)

@main.route('/scholarships')
@jwt_required()
def scholarships():
    scholarships = Scholarship.query.all()
    return render_template('scholarships.html', scholarships=scholarships)