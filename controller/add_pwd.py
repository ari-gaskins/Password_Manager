import mysql.connector
import os
from getpass import getpass
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from model.Data import Data



# collect database
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
user = d.set_user()


# insert collected attributes into table
# table_query = f'INSERT INTO {TABLE} VALUE ({}, {}, {});'
# cursor.execute(table_query)
# for table in cursor:
       # print(table)