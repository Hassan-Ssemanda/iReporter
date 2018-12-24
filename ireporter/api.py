from flask import Blueprint, request, jsonify
from ireporter.models import *
from datetime import datetime


bp = Blueprint('api', __name__, url_prefix='/api/v1')

users = [{'userId': 1, 'firstname': 'Hassan', 'lastname': 'Ssemanda', 'othernames': 'None',  'email': 'hassan@email.com', 'phonenumber': 256777888999, 'username': 'Hassan', 'isAdmin': True},\
{'userId': 2, 'firstname': 'Bob', 'lastname': 'Magembe', 'othernames': 'John',  'email': 'bob@email.com', 'phonenumber': 256777444999, 'username': 'Bob', 'isAdmin': False}]

@bp.route('/users', methods=['POST'])
def register_user():
    # registers a  new user
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othernames = data.get('othernames') 
    email = data.get('email')
    phonenumber = data.get('phonenumber')
    username = data.get('username')
    isAdmin = data.get('isAdmin')

    user = User(firstname, lastname, othernames,  email, phonenumber, username)
    users.append(user)
    return jsonify({
        'status': 201,
        'data': {
            'id': data['userId'],
            'message': 'User created'
        }
    })

@bp.route('/users', methods=['GET'])
def fetch_users():
    # fetches all users    
    try:
        return jsonify({
        'status': 200,
        "users": users
        }), 200
    except:
        return jsonify({
        'status': 404,
        "users": 'no user found'
        }), 404


@bp.route('/users/<int:userId>', methods=['GET'])
def get_user_details(userId):
    for user in users:
        if user['userId'] == userId:
            return jsonify({
                'status': 200,
                'user': user
            }), 200
        return jsonify({
            'status': 400,
            "message": "user id provided is out of range "}), 400   


@bp.route('/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    # this function enables user to delete his/her account
    for user in users:
        if user['userId'] == userId:
            users.remove(user)
            return jsonify({
                'status': 200,
                "message": "account successfully deleted"
            }), 200
        return jsonify({
            'status': 400,
            "message": "account not found "}), 400


redflags = [{'flag_Id': 1, 'incidentType': 'redflag', 'comment':'CAO taking bribes', 'location_lat': 23.1225, 'location_long': 0.2325, 'image': 'cao.jpg' , 'video': 'cao.mpgv'},\
            {'flag_Id': 2, 'incidentType': 'redflag', 'comment':'HR soliciting sexual favours', 'location_lat': 24.1225, 'location_long': 0.2525, 'image': 'df.jpg' , 'video': 'fg.mpgv'}]

@bp.route('/', methods=['GET'])
def index():
    return jsonify({
        'IReporter': "On this platform any one can bring any form of corruption or anythning that requires intervation of authorities and the general public."
    }), 200


@bp.route('/redflag/create', methods=['POST'])
def addRedflag():    
    data = request.get_json()    
    redflag = Redflag(data['flag_Id'], data['incidentType'], data['comment'],
                    data['location_lat'], data['location_long'], data['image'],
                    data['video'])
    redflags.append(redflag)
    return jsonify({
        'status': 201,
        "message": " Successfully created"
    }), 201


@bp.route('/redflags', methods=['GET'])
def returnAll():
    return jsonify({
        'status': 200,
        'redflags':redflags
    }), 200


@bp.route('/redflags/<int:flag_Id>', methods=['GET'])
def getflag(flag_Id):
    for redflag in redflags:
        if redflag['flag_Id'] == flag_Id:
            return jsonify({
                'status': 200,
                "redflag": redflag
            }), 200
        return jsonify({
            'status': 400,
            "message": "redflag id provided is out of range "}), 400

@bp.route('/redflags/<int:flag_Id>', methods=['DELETE'])
def removeRedflag(flag_Id):
    for redflag in redflags:
        if redflag['flag_Id'] == flag_Id:
            redflags.remove(redflag) 
            return jsonify({
                'status' : 200,
                'message':'redflag deleted succesfuly'
            }), 200
        return jsonify({
            'status' : 400,
            'error':'redflag not found'
        }), 400 

@bp.route('/redflags/<int:flag_Id>', methods=['PUT'])
def editSpecificFlag(flag_Id):
    data = request.get_json()
    for redflag in redflags:
        if redflag['flag_Id'] == flag_Id:
            redflag['record_type'] = data['record_type']
            redflag['comment'] = data['comment']
            redflag['location_lat'] = data['location_lat']
            redflag['location_long'] = data['location_long']
            redflag['image'] = data['image']
            redflag['video'] = data['video']
        return jsonify({
            'status': 200,
            'message': "successfully edited"
        }), 200

    return jsonify({
            'status': 403,
            'message': 'operation not allowed'
        }), 403

