# User Management API (Flask + MySQL)

This project is a **User Management API** built with **Flask** and **MySQL**.  
The main purpose of this repository is to represent my **backend development journey**, starting from a clean and structured CRUD API and evolving into more advanced versions.

### Project Evolution

- v1.0 → Basic API
- v1.1 → JWT Authentication
- v1.2 → Middleware Authentication (By Decorators)
- v1.3 → Password hashing
- v2.0 → Logging system
- v2.1 → Pagination
- v2.2 → Filtering
- v2.3 → Pool connection 
- v3.0 → Role-Based Authorization (RBAC)
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
## ✔ Logging system  
- I added to my API project a logging system to monitor my project form loginig and signing in . it save every error and important information in a files inside the log folder .

- I added alse a request logger to montior every request and respond  by useing the request hooks [after_request _ before_request] .

## ✔ Pool connection 

- I make the connection with the database server in the V2.3 esyer than last versions with pooling connection .

## ✔ Role-Based Authorization (RBAC)

- It's kind of authorization based of the user role  not just on admin i made it in this version more public with  and with premitions 

---

## 📁 Project Structure
project/
|──app/
|  ├── core/
|  │ ├── auth_middleware.py
|  │ ├── error_handler.py
|  │ └── errors.py
|  │ ├── logger.py
|  │ ├── request_logger.py
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
|  │ ├── hash.py (it's from v1.3)
|  │
|  │── init.py
|  ├── config.py
|  ├── database.py
|──logs/
|  ├── app.log
|──.env
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
### GET /users ? page = x & limit = y & role = z

Retrieve all users in the page x by limit y and filter the result by role ["admin" or "user"].
Defult (/users) page = 1 limit = 10 users in one page .


### GET /user/id/<id>

Retrieve user by ID.

### GET /user/email/<email>

Retrieve user by email.

### POST /user/ add

Create new user.

### PUT /user/update/<id>

Update user.

### DELETE /user/<id>

Delete user.

### PUT /add/admin/<id> 
To update the user role to admin .
>> just for the admins rloe .

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

- Password hashing --> done ✔

- Logging system --> done ✔

- Pagination --> done ✔

- Filtering  --> done ✔

- Pool connection --> done ✔

- Role-based authorization --> done ✔

- Rate limiting

- Query Optimization

- Docker containerization

…and more.

---

## 📄 License

>This project is part of my backend training path and is open for learning & improvement.
