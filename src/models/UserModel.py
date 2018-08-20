from marshmallow import fields,schema
import datetime
from . import db,bcrypt


class UserModel(db.Model):
    """
    user model

    """
    print("this is user model")
    __tablename__="users"
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    password=db.Column(db.String)
    created_at=db.Column(db.String)

    def __init__(self,data):
        self.name=data.get("name")
        self.password=self.__generate_hash(data.get("password"))
        self.created_at=datetime.datetime.utcnow()

    def __generate_hash(self,password):
        return bcrypt.generate_password_hash(password,rounds=10).decode("utf-8")


    def save(self):
        db.session.add(self)
        db.session.commit(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_user_by_id(id):
        return UserModel.query.get(id)

    
    def __repr(self):
        return '<id {}>.format(self.id)'


class UserSchema():
    """
    user schema
    """
    id=fields.Integer(dump_only=True)
    name=fields.Str(required=True)
    created_at=fields.DateTime(dump_only=True)