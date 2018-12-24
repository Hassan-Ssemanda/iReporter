class Redflag:
    redflags = []
    flag_counter = 1
    def __init__(self, flag_Id, incidentType, comment, location_lat, location_long, image, video):
        self.flag_Id = Redflag.flag_counter      
        Redflag.flag_counter += 1
        self.incidentType = 'redflag'
        self.comment = comment
        self.location_lat = location_lat
        self.location_long = location_long
        self.image = image
        self.video = video

    def get_flag(self):
        # this function gets user details
        return {
            'flag_Id':self.flag_Id,
            'incidentType': self.incidentType,
            'comment': self.comment,
            'location_lat': self.location_lat,
            'location_long': self.location_long,
            'image': self.image,
            'video': self.video
        }

users =[]

class User():    
    user_counter = 1

    def __init__(self, userId, firstname, lastname, othernames,  email, phonenumber, username, isAdmin):
        self.userId = User.user_counter        
        User.user_counter += 1

        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phonenumber = phonenumber
        self.username = username        
        self.isAdmin = False

    def get_user(self):
        # this function gets user details
        return {
            "userId": self.userId,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "username": self.username,
            "isAdmin": self.isAdmin
        }

    def add_user(self):
        users.append(user)








        
