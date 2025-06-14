
# 🧑‍💻 Flask SQLAlchemy User API

A simple RESTful API built with Flask and SQLAlchemy to perform basic CRUD operations on a `User` model.

---

## 📦 Features

- Create a new user
- Get all users
- Get a single user by ID
- Update a user by ID
- Delete a user by ID
- Error handling and safe database commits



---

## 📮 API Endpoints

| Method | Endpoint | Description         |
| ------ | -------- | ------------------- |
| GET    | `/`      | Get all users       |
| GET    | `/<id>`  | Get user by ID      |
| POST   | `/`      | Create a new user   |
| PUT    | `/<id>`  | Update a user by ID |
| DELETE | `/<id>`  | Delete a user by ID |



## 📘 Example User JSON

```json
{
  "name": "Arun",
  "age": 21
}
```
---

## 🔧 Setup Instructions

1. **Clone the repo**



2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
flask run
```

App runs on `http://127.0.0.1:5000/`


---

