from datetime import datetime
from flask import Blueprint, jsonify, make_response, request, abort

from ireporter.models import *

bp = Blueprint('api', __name__, url_prefix='/api/v1')

users = [
    {
        'id': 1, 
        'firstname': 'Hassan', 
        'lastname': 'Ssemanda', 
        'othernames': '',  
        'email': 'hassan@email.com', 
        'phonenumber': 256777888999, 
        'username': 'Hassan', 
        'isAdmin': True,
        "registered": "Thu, 03 Jan 2019 13:57:26 GMT",
    },
    {
        'id': 2, 
        'firstname': 'Bob', 
        'lastname': 'Magembe', 
        'othernames': 'John',  
        'email': 'bob@email.com', 
        'phonenumber': 256777444999, 
        'username': 'Bob', 
        'isAdmin': False,
        "registered": "Thu, 03 Jan 2019 15:05:26 GMT",
    }
]

@bp.route('/users', methods=['GET'])
def get_users():
    # diaplays all users
    return jsonify({
    'status': 200,
    "users": users
    }), 200

@bp.route('/users/<int:userId>', methods=['GET'])
def get_user(userId):
    user = [user for user in users if user['id'] == userId]    
    if len(user) == 0:
        return jsonify({
            'status': 400,
            "message": "user id provided is out of range "
        }), 400
    return jsonify({
            'status': 200,
            'user': user[0]
        }), 200
      
        
@bp.route('/users', methods=['POST'])
def register_user():
    # registers a  new user
    if not request.json or not 'username' in request.json:
        return jsonify({
            'status': 400,
            'error': 'Bad Format'}), 400
    user = {
        'id': users[-1]['id'] + 1,
        'firstname': request.json('firstname'),
        'lastname': request.json('lastname'),
        'othernames': request.json('othernames') ,
        'email' : request.json('email'),
        'phonenumber': request.json('phonenumber'),
        'username': request.json('username'),
        'isAdmin': False,
        'registered': datetime.now()
    }    
    users.append(user)
    return jsonify({
        'status': 201,
        'data': {
            'id': user['id'],
            'message': 'User created'
        }
    }), 201


@bp.route('/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    # this function enables user to delete his/her account
    user = [user for user in users if user['id'] == userId]
    if len(user) == 0:
        return jsonify({
            'status': 400,
            "message": "account not found "
        }), 400
    users.remove(user[0])
    return jsonify({
        'status': 200,
        "message": "account successfully deleted"
    }), 200

@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(userId):
    user = [user for user in users if user['id'] == userId]
    if len(user) == 0:
        return jsonify({
            'status': 404,
            'error': 'No record found'
            }), 404        
    if not request.json:
        return jsonify({
            'status': 404,
            'error': 'Data should be in json format'
        }), 400

    user[0]['firstname'] = request.json.get('firstname', user[0]['firstname'])
    user[0]['lastname'] = request.json.get('lastname', user[0]['lastname'])
    user[0]['othernames'] = request.json.get('othernames', user[0]['othernames'])
    user[0]['email'] = request.json.get('email', user[0]['email'])
    user[0]['phonenumber'] = request.json.get('phonenumber', user[0]['phonenumber'])
    return jsonify({'user': user[0]})
    
@bp.route('/', methods=['GET'])
def index():
    return jsonify({
        'IReporter': "On this platform any one can bring any form of corruption or anythning that requires intervation of authorities and the general public."
    }), 200

redflags = [
    {
        'id': 1,
        'type': 'redflag',
        'comment': u'Buy groceries',
        'images': u'image1',
        'videos': u'video1',
        'location': u'location cordinates',
        'status': 'draft',
        "createdOn": "Wed, 02 Jan 2019 15:36:03 GMT"
    },
    {
        'id': 2,
        'type': 'redflag',
        'comment': u'Learn Python',
        'images': u'image2',
        'videos': u'video2',
        'location': u'location cordinates',
        'status': 'draft',
        "createdOn": "Wed, 02 Jan 2019 16:36:03 GMT"
    }
]

@bp.route('/redflags', methods=['POST'])
def create_redflag():    
    if not request.json or not 'comment' in request.json:
        return jsonify({
            'status': 400,
            'error': 'Bad Request'
        }), 400

    redflag = {
        'id': redflags[-1]['id'] + 1,
        'type': 'redflag',
        'comment': request.json['comment'],
        'images': request.json.get('images'),
        'videos': request.json.get('videos'),
        'location': request.json.get('location'),
        'status': 'draft',
        'createdOn': datetime.now()
    }
    redflags.append(redflag)
    return jsonify({
        'status': 201,
        "message": " Successfully created",
        'redflag': redflag
    }), 201


@bp.route('/redflags', methods=['GET'])
def get_redflags():
    return jsonify({
        'status': 200,
        'redflags':redflags
    }), 200


@bp.route('/redflags/<int:flag_Id>', methods=['GET'])
def get_redflag(flag_Id):
    redflag = [redflag for redflag in redflags if redflag['id'] == flag_Id]
    if len(redflag) == 0:
        return jsonify({
            'status': 400,
            "message": "redflag id provided is out of range "}), 400
    return jsonify({
        'status': 200,
        "redflag": redflag[0]
    }), 200
    

@bp.route('/redflags/<int:flag_Id>', methods=['DELETE'])
def delete_redflag(flag_Id):
    redflag = [redflag for redflag in redflags if redflag['id'] == flag_Id]
    if len(redflag) == 0:
        return jsonify({
            'status' : 400,
            'error':'redflag not found'
        }), 400 
    redflags.remove(redflag[0])   
    return jsonify({
        'status' : 200,
        'message':'redflag deleted succesfuly'
    }), 200
        

@bp.route('/redflags/<int:flag_Id>', methods=['PUT'])
def update_redflag(flag_Id):
    redflag = [redflag for redflag in redflags if redflag['id'] == flag_Id]
    if len(redflag) == 0:
        return jsonify({
            'status': 404,
            'error': 'No record found'
            }), 404
    if not request.json:
        return jsonify({
            'status': 400,
            'error': 'Data should be in json format'
            }), 400

    redflag[0]['type'] = request.json.get('type', redflag[0]['type'])
    redflag[0]['comment'] = request.json.get('comment', redflag[0]['comment'])
    redflag[0]['images'] = request.json.get('images', redflag[0]['images'])
    redflag[0]['videos'] = request.json.get('videos', redflag[0]['videos'])
    redflag[0]['location'] = request.json.get('location', redflag[0]['location'])
    redflag[0]['status'] = request.json.get('status', redflag[0]['status'])
    return jsonify({
        'status': 200,
        'message': 'successfully edited',
        'redflag':redflag[0]
    }), 200