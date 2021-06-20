import mysql.connector
import os
from dotenv import load_dotenv

# collect user and passwd values for connection
load_dotenv()
USERNAME = os.getenv('USERNAME')
MASTER_PASSWORD = os.getenv('MASTER_PASSWORD')

# establish connection to database
database = mysql.connector.connect(
        host='localhost',
        user=USERNAME, 
        passwd=MASTER_PASSWORD
        )
# create cursor for queries
cursor = database.cursor()
