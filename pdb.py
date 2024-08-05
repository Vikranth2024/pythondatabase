import mysql.connector
dbs = ["mydb1","mydb2","mydb3"]
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
c1 = db.cursor()
for i in dbs:
    c1.execute("CREATE DATABASE "+i)

