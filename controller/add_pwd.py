import mysql.connector
import os
from getpass import getpass
from cryptography.fernet import Fernet
from dotenv import load_dotenv



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


# insert collected attributes into table
# table_query = f'INSERT INTO {TABLE} VALUE ({}, {}, {});'
# cursor.execute(table_query)
# for table in cursor:
       # print(table)