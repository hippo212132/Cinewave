import sqlite3, hashlib
from user import user

connection = sqlite3.connect("RolsaTech.db", check_same_thread=False) #Connects to the DB file using SQLITE3 Connections

#Establishing Connection to Database

cur = connection.cursor()

def hash(phrase): #This is a function used to hash a new password
 
    object = hashlib.md5(str(phrase).encode())
    object = object.hexdigest()
 
    return object


def createUser(email, username, password, phone):

    password = hash(password) #Uses the hash function on the password before its executed to the database

    cur.execute("INSERT INTO USERS (email, username, password, phone) VALUES (?,?,?,?)", (email, username, password, phone))
    connection.commit()

    id = cur.lastrowid

    return user(id, email, username, password, phone)