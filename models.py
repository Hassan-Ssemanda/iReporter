class Record:
    def __init__(self, record_id, createdOn, createdBy, record_type, comment,
                 description, location, status, images, videos, comments):
        self.record_id = record_id
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.record_type = record_type
        self.comment = comment
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos

    def getRecord(self):
        return {
            "record_id": self.record_id,
            "created_on": self.createdOn,
            "createdBy": self.createdBy,
            "record_type": self.record_type,
            "comment": self.comment,
            "location": self.location,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
        }


class User:
    def __init__(self, user_id, firstname, lastname, othernames, email,
                 phonenumber, username, registeredOn, password):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phonenumber = phonenumber
        self.username = username
        self.password = password
        self.registeredOn = registeredOn

    def getUserDetails(self):
        return {
            "user_id": self.user_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            " othernames": self.othernames,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "username": self.username,
            "registeredOn": self.registeredOn,
        }