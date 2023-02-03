from bookstore_app import app
from bookstore_app.models import Author
from flask import jsonify

@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    print(authors)
    return jsonify({
        'success': True,
        'data': 'get all authors'
    })

@app.route('/api/v1/authors', methods=['POST'])
def create_authors():
    return jsonify({
        'success': True,
        'data': 'Author has been created successfully'
    }), 201

@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id:int):
    return jsonify({
        'success': True,
        'data': f'get author with id: {author_id}'
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id:int):
    return jsonify({
        'success': True,
        'data': f'Author with id: {author_id} has been updated'
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id:int):
    return jsonify({
        'success': True,
        'data': f'Author with id: {author_id} has been deleted'
    })
