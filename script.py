import mysql.connector

#establish a connection to the Mysql server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sgt2023",
    database="example"
)

#Create a new table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mydb.commit()