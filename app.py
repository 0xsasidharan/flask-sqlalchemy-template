from flask import Flask ,request 
from flask_sqlalchemy import SQLAlchemy
from schema import UserSchema , UserUpdateSchema
from marshmallow import ValidationError

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }

user_schema= UserSchema()
users_schema = UserSchema(many=True)
update_schema =UserUpdateSchema()

@app.get("/")
def get_all_users():
    users = User.query.all()
    return users_schema.dump(users)

@app.get("/<string:id>")
def get_one_users(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "User not found"}, 404

    return user_schema.dump(user)

@app.put("/<string:id>")
def edit_one_users(id):
    request_data = request.get_json()
    try:
        data = update_schema.load(request_data)
    except ValidationError as err:
        return {"message": "Input error", "errors": err.messages}, 400
    
    user = User.query.get(id)
    if user is None:
        return {"error": "User not found"}, 404
    
    if "name" in data:
        user.name = data["name"]
    if "age" in data:
        user.age = data["age"]

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return {"error": "Database error"}, 500

    return user_schema.dump(user)


@app.post("/")
def add_user():
    request_data = request.get_json()

    try:
        data = user_schema.load(request_data)
    except ValidationError as err:
        return {"message": "Input error", "errors": err.messages}, 400
    
    name = data["name"]
    age = data["age"] 
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return {"error": "Database error"}, 500

    return user_schema.dump(new_user)

@app.delete("/<string:id>")
def delete_one_user(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "User not found"}, 404

    db.session.delete(user)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return {"error": "Database error"}, 500

    return {"message" : "User deleted successfully"}





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()