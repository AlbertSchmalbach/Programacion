import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwod = "As_21048"
)

print(mydb)

