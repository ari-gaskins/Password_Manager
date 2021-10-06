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
    
    def get_user(self):
       self.usr = input('Enter new username to add: ')
       return self.usr
    
    def get_pwd(self):
        self.pwd = getpass('Enter new password to add: ')
        return self.pwd

    def get_site(self):
        self.site = input('Enter website to add: ')
        return self.site
    
    def get_email(self):
        self.email = input('Enter email associated with site: ')
        if self.email is None:
            pass
        else:
            return self.email

    def get_bkup_em(self):
        self.bkup_em = input('Enter backup email associated with site: ')
        if self.bkup_em is None:
            pass
        else:
            return self.bkup_em

    def get_key(self):
        self.key = Fernet.generate_key()
        return self.key