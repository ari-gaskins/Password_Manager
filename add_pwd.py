import mysql.connector
import os
from getpass import getpass
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from Pwd_Property import Pwd_Property


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
                print(connection)
except Exception as e:
        print(e)

# create cursor for queries
cursor = connection.cursor()

def create_key():
        key = Fernet.generate_key()
        return key

# get inputs
username = input('Enter new username to add: ')
password = getpass('Enter new password to add: ')
website = input('Enter website to add: ')
key = create_key()

# create new pwd property object and set values
p = Pwd_Property()
p.user = username
p.pwd = password
p.site = website
p.key = key

# create table query and add values
table_query = f'INSERT INTO {TABLE} VALUE ({p.user}, {p.pwd}, {p.site});'
cursor.execute(table_query)
for table in cursor:
        print(table)