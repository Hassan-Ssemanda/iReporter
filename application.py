from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

records = []


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/')
def recordCreate():
    return render_template('recordCreate.html')

@app.route('/intervation')
def intervation():
    return render_template('intervation.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# API end points
@app.route('/api/v1/records', methods=['POST'])
def createRecord():
    # Creates a new record
    data = request.get_json()
    record_id = len(records)+1
    createdOn = datetime.now()
    record = Record(record_id, data['title'], data['description'],
                    data['status'], data['comments'],
                    createdOn, data['location'], data['record_type'],
                    data['images'], data['videos'], data['created_by'])
    records.append(record)
    return jsonify({"message": " record successfully created "}), 201

@app.route('/api/v1/records', methods=['GET'])
def userRecords():
    # Fetch all user's records
    Records = [record.get_record() for record in records]
    return jsonify({"records": Records})

@app.route('/api/v1/records/<int:record_id>', methods=['GET'])
def userRecord(record_id):
    # Fetch a specific record
    user_record = []
    record = records[record_id - 1]
    user_record.append(record.get_record())
    return jsonify({"record": user_record}), 200

@app.route('/api/v1/records/<int:record_id>', methods=['PUT'])
def editRecord(record_id):
    # editing a record
    if  record_id > len(records) or record_id < 0:
        return jsonify({"message": "Index is out of range"}), 400
    data = request.get_json()
    for record in records:
        if int(record.record_id) == int(record_id):
            record.record_type = data['record_type']
            record.title = data['title']
            record.description = data['description']
            record.location = data['location']
            record.status = data['status']
            record.images = data['images']
            record.videos = data['videos']
            record.created_by = data['created_by']
    return jsonify({'message': "successfully edited"}), 200


@app.route('/api/v1/records/<int:record_id>', methods=['DELETE'])
def deleteRecord(record_id):
    # this function enables user delete record
    if record_id <= 0 or record_id > len(records):
        return jsonify({"message": "Index out of range"}), 400
    for record in records:
        if record.record_id == record_id:
            records.remove(record)
    return jsonify({"message": "record successfully deleted"}), 200

users = []


@app.route('/api/v1/users', methods=['POST'])
def registerUser():
    # registers a  new user
    data = request.get_json()
    user_id = len(users)+1
    registeredOn = datetime.now()
    user = User(user_id, data['firstname'], data['lastname'],
                data['othernames'], data['email'], data['phonenumber'],
                data['username'], registeredOn)
    users.append(user)
    return jsonify({"message": " account has been successfully created"}), 201


@app.route('/api/v1/users', methods=['GET'])
def fetchUsers():
    # fetches all user's records
    user = [user.getUserDetails() for user in users]
    return jsonify({"users": user})


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
# this fetches a single user account
def fetchUserDetails(user_id):
    fetched_user = []
    user = users[user_id - 1]
    fetched_user.append(user.getUserDetails())
    return jsonify({"user": fetched_user}), 200


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    # this function enables user to delete his/her account
    if user_id <= 0 or user_id > len(users):
        return jsonify({"message": "Index out of range"}), 400
    for user in users:
        if user.user_id == user_id:
            users.remove(user)
    return jsonify({"message": "account successfully deleted"}), 200

