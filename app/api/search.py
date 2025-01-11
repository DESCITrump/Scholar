from flask import jsonify, request
from app.models import Document
from . import api
from flask_jwt_extended import jwt_required
import whoosh.index
from whoosh.qparser import QueryParser

@api.route('/search', methods=['GET'])
@jwt_required()
def search_documents():
    search_term = request.args.get('q', '')
    ix = whoosh.index.open_dir("indexdir")
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(search_term)
        results = searcher.search(query)
        return jsonify([{"id": r['id'], "title": r['title']} for r in results])