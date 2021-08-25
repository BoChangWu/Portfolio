from flask import Flask, request,jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from lotify.client import Client

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
class Members(db.Model):
    
    __tablename__= 'members'

    mid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    mname=db.Column(db.String(50))
    memail=db.Column(db.String(50))
    mpwd = db.Column(db.String(300))

    def __init__(self,mname,memail,mpwd):
        self.mname = mname
        self.memail = memail
        self.mpwd = bcrypt.generate_password_hash(mpwd)

    def __repr__(self):
        return f'Name:{self.mname},Email:{self.memail}'



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
class MembersSchema(ma.Schema):
    class Meta:
        fields = (
            'mid',
            'mname',
            'memail',
            'mpwd',
        )
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

member_schema = MembersSchema()
members_schema = MembersSchema(many=True)

company_schema = CompanysSchema()
companys_schema = CompanysSchema(many=True)

# APIs

class EmailCheck(Resource):

    def get(self):
        memail = request.json['memail']
        member = Members.query.filter_by(memail=memail).first()
        if member:
            return{'Message': 'This email already taken'}

# class Login(Resource):

#     def post(self):
#         memail = request.json['memail']
#         mpwd = request.json['mpwd']

#         member = Members.query.filter_by(memail=memail)
#         if member:
#             pwd = Members.query.filter_by(
#                 memail=memail).with_entities(Members.mpwd)
#             result = member_schema.dumps(pwd)
#             print(result)
#             result_json = json.load(result)
#             password = bcrypt.check_password_hash(result_json['mpwd'],mpwd)

#             if not password:
#                 return {'Message': 'Wrong password'}
#             else:
#                 return{'Message' : 'Member does not exist'}

class Register(Resource):

    def post(self):
        mname = request.json['mname']
        memail = request.json['memail']
        mpwd = request.json['mpwd']
        member = Members(mname,memail,mpwd)
        db.session.add(member)
        db.session.commit()
        return member_schema.jsonify(member)

class ShowMembers(Resource):

    def get(self):
        all_members = Members.query.all()
        results = members_schema.dump(all_members)
        return jsonify(results)        

class GetMsg(Resource):
    def get(show):
        all_msgs= Companys.query.all()
        results = companys_schema.dump(all_msgs)
        return jsonify(results)


#line notify
user_token = '7nE57TPaLZYdzKz5KR1cVFcR1YxchFvBXo4Ypkm7XQ1'
client_id = 'QTIJkTFC5nX2SBU0fCUAMi'
client_secret = 'HHf9wfwQv4NDCxjdaWkOfuFGa6wGUhC9DrDdvGf9Pxc'
lo_uri = 'http://127.0.0.1:5000/lotify'


class SendText(Resource):

    def post(self):
        response_object={
            "message": '',
        }
        cname = request.json['cname']
        csubject = request.json['csubject']
        cphone = request.json['cphone']
        cemail = request.json['cemail']
        cmessage = request.json['cmessage']
        company = Companys(cname,csubject,cphone,cemail,cmessage)
        db.session.add(company)
        db.session.commit()

        MESSAGE= f'hello, I am {cname},from {csubject},heres my phone:{cphone} and email: {cemail},I wanna say {cmessage}'

        lotify = Client(client_id=client_id,
        client_secret=client_secret, redirect_uri=lo_uri)
        status = lotify.status(access_token=user_token)

        if status['status'] == 200:
            response = lotify.send_message(access_token=user_token, message=MESSAGE)
        response_object['message'] = 'Message sent!'
        return company_schema.jsonify(company)

#add api route
api.add_resource(SendText,'/sendtext')
api.add_resource(GetMsg,'/getmsg')
api.add_resource(EmailCheck,'/emailcheck')
# api.add_resource(Login,'/login')
api.add_resource(Register,'/register')
api.add_resource(ShowMembers,'/showmembers')



if __name__=='__main__':
    app.run(debug=True)
