## Midterm Project - Flask application 

### Ishan Jawade    
CWID: 885186304     Email: ishanjawade@csu.fullerton.edu

![Screenshot](./images/PostmanScreenshot.png)

## **Features**
A RESTful API built with Flask and MongoDB that supports:
- User authentication (JWT)
- File uploads (authenticated)
- Public/private routes
- CRUD operations for items

## **Prerequisites**
- Python 3.8+
- MongoDB (local or cloud URI)
- venv (recommended)

## **Setup**
1. **Clone the repository**
    ```bash
    git clone https://github.com/IshanJawade/midterm-project.git
    cd midterm-project

2. **Download dependencies**
    ```bash
    pip install -r requirements.txt

3. **Run the application**
    ```bash
    python app.py

## API Endpoints

| Endpoint                     | Method | Auth Required | Description                        |
|------------------------------|--------|---------------|------------------------------------|
| `/auth/login`                | POST   | No            | Login to get JWT token             |
| `/auth/register`             | POST   | No            | Register new user                  |
| `/auth/upload`               | POST   | Yes           | Upload file (JWT required)         |
| `/auth/items`                | POST   | Yes           | Create new item                    |
| `/auth/items/<item_id>`      | PUT    | Yes           | Update item by ID                  |
| `/auth/items/<item_id>`      | DELETE | Yes           | Delete item by ID                  |
| `/public/items`              | GET    | No            | List all items (public)            |

Copyrights Ishan Jawade 2025
