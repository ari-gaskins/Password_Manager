# import the sql.connector
import  mysql.connector
from getpass import getpass

# establish connection to database
database = mysql.connector.connect(
        host='localhost',
        user=input('Enter username: '), 
        passwd=getpass('Enter password: ')
        )
# create cursor for queries
cursor = database.cursor()

# show the databases we have access to 
show_db_query = cursor.execute('SHOW DATABASES;')
cursor.execute(show_db_query)
for db in cursor:
    print(db)
