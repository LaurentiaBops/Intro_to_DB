import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "/~M8UL7(4YMn)3"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print(f"Database 'alx_book_store' created successfully!")
        
except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    mycursor.close()
    mydb.close()