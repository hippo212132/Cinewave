import sqlite3, hashlib, random, string
from user import user

connection = sqlite3.connect("RolsaTech.db", check_same_thread=False) #Connects to the DB file using SQLITE3 Connections

#Establishing Connection to Database

cur = connection.cursor()

def hash(phrase): #This is a function used to hash a new password
 
    object = hashlib.md5(str(phrase).encode())
    object = object.hexdigest()
 
    return object


def createUser(username, email, password):

    password = hash(password) #Uses the hash function on the password before its executed to the database

    len = 15
    
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=len))


    cur.execute("INSERT INTO Users(ID, Username, Email, Password) VALUES (?,?,?,?)", (id, username, email, password))
    connection.commit()

    

    return user(id, username, email, password)