from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv
import json

load_dotenv()

# create an app and add middlewares
app = Flask(__name__)
CORS(app)
api= Api(app)

#config
# mySQL DB   給的值 為 username:password@localhost/db_name
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.environ.get("MYSQL_USER")}:{os.environ.get("MYSQL_PASSWORD")}@{os.environ.get("MYSQL_HOST")}/{os.environ.get("MYSQL_DATABASE")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
ma= Marshmallow(app)

#for password hashing
bcrypt = Bcrypt(app)

#models

class Companys(db.Model):
    
    __tablename__ = 'companys'

    cid= db.Column(db.Integer,primary_key=True, autoincrement=True)
    cname = db.Column(db.String(50))
    csubject = db.Column(db.String(50))
    cphone = db.Column(db.String(50))
    cemail = db.Column(db.String(300),unique =True,index = True)
    cmessage = db.Column(db.String(3000))
    
    def __init__(self,cname,csubject,cphone,cemail,cmessage):
        self.cname = cname
        self.csubject = csubject
        self.cphone = cphone
        self.cemail = cemail
        self.cmessage = cmessage

    def __repr__(self):
        return f'Name:{self.cname},Subject:{self.csubject},Phone: {self.cphone},Email:{self.cemail}'
    

# create schema
class CompanysSchema(ma.Schema):
    class Meta:
        fields = (
            'cid',
            'cname',
            'csubject',
            'cphone',
            'cemail',
            'cmessage'
        )

company_schema = CompanysSchema()
companys_schema = CompanysSchema(many=True)

# APIs

class EmailCheck(Resource):

    def get(self):
        cemail = request.json['cemail']
        company = Companys.query.filter_by(cemail=cemail).first()
        if company:
            return{'Message': 'This email already taken'}


class SendText(Resource):

    def post(self):
        cname = request.json['cname']
        csubject = request.json['csubject']
        cphone = request.json['cphone']
        cemail = request.json['cemail']
        cmessage = request.json['cmessage']
        company = Companys(cname,csubject,cphone,cemail,cmessage)
        db.session.add(company)
        db.session.commit()
        return company_schema.jsonify(company)

#add api route
api.add_resource(SendText,'/sendtext')


if __name__=='__main__':
    app.run(debug=True)
