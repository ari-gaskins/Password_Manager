# Password Property class in order to add security to projec
# and to incorporate OOP

class Pwd_Property(object): 

    # class attribute/instance variables
    number_of_properties = 0

    # set up for a pwd property object
    def __init__(self, user, pwd, site, key):
        self.user = user
        self.pwd = pwd
        self.site = site
        self.key = key
        # increments number of pwd properties
        Pwd_Property.add_property()

    # class methods used to increment on the number or properties
    # only effects class itself, used to keep track
    @classmethod
    def get_number_of_properties(cls):
        return cls.number_of_properties
    
    @classmethod
    def add_property(cls):
        cls.number_of_properties += 1

    # getter methods for property values
    @property
    def username(self):
        return self.user

    @property
    def password(self):
        return self.pwd

    @property
    def website(self):
        return self.site
    
    @property
    def encryption_key(self):
        return self.encryption_key
    
    # setter methods for property values
    @username.setter
    def username(self, usr):
        self.user = usr
    
    @password.setter
    def password(self, pd):
        self.pwd = pd
    
    @website.setter
    def website(self, web):
        self.site = web
    
    @encryption_key.setter
    def encryption_key(self, encrypt):
        self.key = encrypt