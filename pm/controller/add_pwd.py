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
        with mysql.connector.connect(
        host='localhost',
        user=input('Enter username: '), 
        passwd=getpass('Enter master password: '),
        database=DATABASE
        ) as connection:
                print('Established connection to database...')
except Exception as e:
        print(e)

# create cursor for queries
cursor = connection.cursor()

# instantiate Data objec
d = Data.Data()
# add attributes
d.set_user()
d.set_pwd()
d.set_email()
d.set_site()
d.set_bkup_em()
d.set_key()


# insert collected attributes into table
# table_query = f'INSERT INTO {TABLE} VALUE ({}, {}, {});'
# cursor.execute(table_query)
# for table in cursor:
       # print(table)