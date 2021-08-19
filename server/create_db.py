import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    passwd="xu04y3m6"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE mymsg")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
