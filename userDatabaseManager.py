import sqlite3
import os 
from tkinter import *
from tkinter import messagebox
from encryptionManager import hashPassword

databaseConnection = sqlite3.connect("WhitmoyerDB")
cursor = databaseConnection.cursor() 

def addUser(username, password):
    try: 
        password = hashPassword(password).hex()
        print("The hashed password: " + password)
        cursor.execute(f"INSERT INTO User VALUES ('{username}', '{password}')")
        databaseConnection.commit()
    except Exception as e:
        print("Failed to add user: ", e)

def addCreditCard(username, creditcard):
    try: 
        cursor.executescript(f"INSERT INTO Creditcard VALUES ('{username}', '{creditcard}')")
        databaseConnection.commit()
    except Exception as e:
        print("Failed to add credit card: ", e)

def createDefaultDatabase():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS User(username VARCHAR PRIMARY KEY, password VARCHAR)")
        addUser("SuperAdmin", "123456")
        addUser("KatherineWhitmoyer", "Password")
        addUser("Steve", "111111")
        addUser("Bill", "aaaaaa")
        databaseConnection.commit()
    except Exception as e: 
        print("Failed to create table add default users to user table")

    #Creates seperate, supposedly 'unaccessable' table with high attractive data for UNION SELECT attack 
    try: 
        cursor.execute("CREATE TABLE IF NOT EXISTS Creditcard(username VARCHAR PRIMARY KEY, creditcardnumber VARCHAR)")
        addCreditCard("SuperAdmin", "1341 2525 3235 5235")
        addCreditCard("KatherineWhitmoyer", "2352 3342 4264 2464")
        addCreditCard("Steve", "2352 2524 2355 2352")
        addCreditCard("Bill", "1341 5235 2453 1351")
        databaseConnection.commit()
    except Exception as e:
        print("Failed to create credit cards for users.")
        
def checkPassword(username, password):
    try: 
        password = hashPassword(password).hex()
        query = f"SELECT * FROM User WHERE Username = '{username}' AND password = '{password}'"
        checkPassword = cursor.execute(query)
        passwordFound = checkPassword.fetchall()
        if len(passwordFound) != 0:
            print("Login successful")
            print(passwordFound)
            messagebox.showinfo("Login Successful", "Login successful!")

            #Print query results for purposes of demonstration 
            print("Query Returns:")
            for entry in passwordFound:
                print(entry)
            
            return True
        else:
            print("Login failed")
            messagebox.showinfo("Login Failed", "Login failed.")
    except Exception as e: 
        print("Failed to check password: ", e)
        #Provides visual of a DROP TABLES sql injection attack in demo video 
        if "no such table: user" in str(e).lower():
            messagebox.showerror("Error", "User table does not exist.")

def checkPasswordForInjection(username, password):
    try: 
        password = hashPassword(password).hex()
        query = f"SELECT * FROM User WHERE Username = '{username}' AND password = '{password}'"
        checkPassword = cursor.executescript(query)
        passwordFound = checkPassword.fetchall()
        if len(passwordFound) != 0:
            print("Login successful")
            print(passwordFound)
            messagebox.showinfo("Login Successful", "Login successful!")

            #Print query results for purposes of demonstration 
            print("Query Returns:")
            for entry in passwordFound:
                print(entry)
            
            return True
        else:
            print("Login failed")
            messagebox.showinfo("Login Failed", "Login failed.")
    except Exception as e: 
        print("Failed to check password: ", e)
        #Provides visual of a DROP TABLES sql injection attack in demo video 
        if "no such table: user" in str(e).lower():
            messagebox.showerror("Error", "User table does not exist.")

#Provides testing functionality, created to test database functions as I wrote them
#Not needed for final project 
if __name__ == "__main__":
    print("Testing database manager...")
    testConnection = sqlite3.connect("WhitmoyerDB")
    testCursor = testConnection.cursor() 

    print("This should return an error if the user table does not exist yet.")
    checkPassword("Steve", "111111")

    print("Creating default database")
    createDefaultDatabase()

    print("The following login should succeed:")
    checkPassword("Steve","111111") #Should return true 
    print("The following login should fail:")
    checkPassword("Evil Steve", "111111") #Should return false 
    print("The following login should fail:")
    checkPassword("Steve", "evilPassword") #Shoudld return false
    print("The following login should fail:") 
    checkPassword("Eve", "EvilPassword") #Should return false 

'''
Academic Integrity Notes:
    The underlying structure of the sqlite database was taken from: https://github.com/evaizalith/flowerpath
    Information on hashing passwords: https://www.tutorialspoint.com/how-to-hash-passwords-in-python

    All sources can be found in sources.md in repo
'''