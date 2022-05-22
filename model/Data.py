from cryptography.fernet import Fernet
from getpass import getpass

# class to collect user data
class Data:

    def __init__(self, usr, pwd, site, email, bkup_em, key):
        self.usr = usr
        self.pwd = pwd
        self.site = site
        self.email = email
        self.bkup_em = bkup_em
        self.key = key
    
    # username getter
    def get_user(self):
       return self.usr

    # username setter
    def set_user(self, u):
        u = input('Enter new username to add: ')
        self.usr = u
    
    # password getter
    def get_pwd(self):
        return self.pwd

    # password setter
    def set_pwd(self, p):
        p = getpass('Enter new password to add: ')
        self.pwd = p

    # website getter
    def get_site(self):
        return self.site
    
    # website setter
    def set_site(self, s):
        s = input('Enter website to add: ')
        self.site = s

    # email getter
    def get_email(self):
        return self.email

    # email setter
    def set_email(self, e):
        e = input('Enter email associated with site: ')
        if e is None:
            pass
        self.email = e

    # backup email getter
    def get_bkup_em(self):
        return self.bkup_em
    
    # backup email setter
    def set_bkup_em(self, b):
        b = input('Enter backup email associated with site: ')
        if b is None:
            pass
        self.bkup_em = b

    # key getter
    def get_key(self): 
        return self.key

    # key setter
    def set_key(self, k):
        k = Fernet.generate_key()
        self.key = k