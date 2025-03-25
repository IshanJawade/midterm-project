from flask import Blueprint, jsonify

public_bp = Blueprint("public", __name__)

@public_bp.route('/public', methods=['GET'])
def public_info():
    public_items = [
        {"id": 1, "name": "Free eBook", "description": "A free guide to Flask development"},
        {"id": 2, "name": "Open Source API", "description": "Access public API documentation"},
        {"id": 3, "name": "Community Forum", "description": "Join discussions with developers"},
    ]
    return jsonify({"message": "Public Information", "data": public_items}), 200
