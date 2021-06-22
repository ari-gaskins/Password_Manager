# import the sql.connector
import  mysql.connector

# establish connection to database
database = mysql.connector.connect(
        host='localhost',
        user='', 
        passwd=''
        )
# create cursor for queries
cursor = database.cursor()

# show the databases we have access to 
show_db_query = cursor.execute('SHOW DATABASES;')
cursor.execute(show_db_query)
for db in cursor:
    print(db)
