# User Management API (Flask + MySQL)

This project is a **User Management API** built with **Flask** and **MySQL**.  
The main purpose of this repository is to represent my **backend development journey**, starting from a clean and structured CRUD API and evolving into more advanced versions.

### Project Evolution

- v1.0 → Basic API
- v1.1 → JWT Authentication
- v1.2 → Middleware Authentication (By Decorators)
- v1.3 → Password hashing

---

## 📌 Features (Current Version)
### ✔ CRUD Operations  
- Create user  
- Retrieve all users  
- Retrieve user by ID  
- Retrieve user by email  
- Update user  
- Delete user  

### ✔ Clean Architecture  
- `models/` → SQL queries  
- `services/` → Business logic  
- `routes/` → Flask Blueprints  
- `utils/` → Validators + response helpers  
- `core/` → Custom errors + error handler  
- `database/` → MySQL connection & query wrapper  

### ✔ Error Handling  
Custom exception system:
- `ValidationError`
- `NotFoundError`
- `AuthenticationError`
- `PermissionError`
- `DatabaseError`

All errors are returned in a consistent JSON format.

### ✔ Input Validation  
The API validates:
- Email format  
- Data types  
- Empty fields  
- Password length  
- JSON body structure  

### ✔ JWT Authentication

- In this version I created a JWT (JSON Web Token) and return it to the user through the login or signup functions.
- I implemented a middleware decorator for authentication that checks whether the JWT in the request is valid or not. I also use it to verify the admin role of the request.

> I improved the authentication concept in my project and added middleware for better security.

### ✔ Save password in safe way  
I delet the password file in app folder couse i put all my passwords in safest way.
I put it in environment variables in the file .env

### ✔ Password hashing  
- I used the bcrypt module to save the users passwords in database in a safe way by 
hashing it . 
- The cod of hashing password and verifeing it in
```bash
utils/hash.py
```

---

## 📁 Project Structure
project/
|──app/
|  ├── core/
|  │ ├── error_handler.py
|  │ └── errors.py
|  │
|  ├── models/
|  │ └── user_model.py
|  │
|  ├── routes/
|  │ └── auth_routes.py
|  │ └── user_routes.py
|  │
|  ├── services/
|  │ └── auth_service.py
|  │ └── user_service.py
|  │
|  ├── utils/
|  │ ├── response.py
|  │ ├── validators.py
|  │
|  │── init.py
|  ├── config.py
|  ├── database.py
|──run.py


---

## 🚀 Running the Project

### 1) Create virtual environment
```bash
python -m venv venv
```
### 2) Activate it

Windows
```bash
venv\Scripts\activate
```

Linux/Mac
```bash
source venv/bin/activate
```
### 3) Install dependencies
```bash
pip install -r requirements.txt
```
### 4) Run the server
```bash
python run.py
```
## 🛢 Database Configuration

Database settings are located in:
```bash
app/config.py
```
For safety, the file:
```bash
.env
``` 
>is ignored and **NOT nincluded** in the repository because it contains your database password.

---

## 🧩 API Endpoints
1. ## user_blueprint
### GET /users

Retrieve all users.

### GET /user/id/<id>

Retrieve user by ID.

### GET /user/email/<email>

Retrieve user by email.

### POST /user/

Create new user.

### PUT /user/<id>

Update user.

### DELETE /user/<id>

Delete user.

2. ## authration_blueprint
## POST /login

To login in the system and return to the user the token .

## POST /signup
To signup in the the system and return a valid token to the user.

---

## 📦 Future Versions

### This project will evolve into multiple advanced releases, including:

- Token-based authentication (JWT) --> done ✔

- Middleware engine --> done ✔

- Password hashing

- Role-based authorization

- Logging system

- Rate limiting


- Docker containerization
…and more.

---

## 📄 License

>This project is part of my backend training path and is open for learning & improvement.
