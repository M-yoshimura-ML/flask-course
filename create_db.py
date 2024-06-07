import mysql.connector

""" This is for your local DB info and to create DB from Python """
mydb = mysql.connector.connect(
   host="localhost",
   port="3306",
   user="admin",
   password="password!123"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS flask_blog CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
   if db == ('flask_blog',):
      print(db)
