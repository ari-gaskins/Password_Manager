import mysql.connector
import os
import sys
from getpass import getpass
from cryptography.fernet import Fernet
from dotenv import load_dotenv


# append path for module import
sys.path.append(r'/home/arikiri/Documents/GitHub/Password_Manager/pm')

# import Data class
from model import Data


# collect database info
load_dotenv()
DATABASE = os.getenv('DATABASE') 
TABLE = os.getenv('TABLE')

# establish connection to database
try:
        connection = mysql.connector.connect(
        host='localhost',
        user=input('Enter username: '), 
        passwd=getpass('Enter master password: '),
        database=DATABASE
        )
        print('Established connection to database...')
except Exception as e:
        print(e)

# create cursor for queries
cursor = connection.cursor()

# instantiate Data objec
d = Data.Data()
# add attributes
d.set_user(input('Enter new username to add: '))
d.set_pwd(getpass('Enter new password to add: '))
d.set_email(input('Enter email associated with site: '))
d.set_site(input('Enter website to add: '))
d.set_bkup_em(input('Enter backup email associated with site: '))
d.set_key(Fernet.generate_key())

user = d.get_user()
pwd = d.get_pwd()
site = d.get_site()
email = d.get_email()
bkup_email = d.get_bkup_em()
key = d.get_key()


# insert collected attributes into table
table_query = f'''INSERT INTO {TABLE} (username, pass_word, website, email, backup_email) 
VALUES (%s, %s, %s, %s, %s);'''
record_data = (user, pwd, site, email, bkup_email)
cursor.execute(table_query, record_data)
connection.commit()