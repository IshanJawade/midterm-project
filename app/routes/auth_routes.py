from flask import Blueprint, request, jsonify, current_app
from app.config import allowed_file
from app.services.auth_service import generate_jwt_token, verify_jwt_token
from app.models.user import User
from app.utils.error_handlers import handle_bad_request, handle_unauthorized, handle_not_found
from app.config import allowed_file 
import os
from werkzeug.utils import secure_filename

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return handle_bad_request("Username and password are required")

    if User.find_user(username):
        return handle_bad_request("Username already exists")

    User.create_user(username, password)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.find_user(username)
    if not user:
        return handle_not_found("User not found")

    if not User.verify_password(user["password"], password):
        return handle_unauthorized("Incorrect password")

    token = generate_jwt_token(username)
    return jsonify({"message": "Login successful", "token": token}), 200

@auth_bp.route('/upload', methods=['POST'])
def upload_file():
    # Authentication check
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return handle_unauthorized("Missing or invalid authorization token")
    
    token = auth_header.split(' ')[1]
    payload = verify_jwt_token(token)
    if not payload:
        return handle_unauthorized("Invalid or expired token")
    
    # File upload handling (your original logic with minor adjustments)
    if 'file' not in request.files:
        return handle_bad_request("No file part")

    file = request.files['file']

    if file.filename == '':
        return handle_bad_request("No selected file")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        
        # Ensure upload directory exists
        os.makedirs(upload_folder, exist_ok=True)
        
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        return jsonify({
            "message": "File uploaded successfully",
            "file_path": file_path,
            "filename": filename
        }), 201
    else:
        return handle_bad_request("Invalid file type or file size too large")
