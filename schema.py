from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)     
    name = fields.Str(required=True)    
    age = fields.Int(required=True)     

class UserUpdateSchema(Schema):
    name = fields.Str()    
    age = fields.Int()     