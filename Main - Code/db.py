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


def checkUser(email,password):

    password = hash(password)

    cur.execute("SELECT * FROM Users WHERE Email = ? AND Password = ?", (email, password))

    return cur.fetchall()

def add_consultation(date, quantity):
    cur.execute('INSERT INTO Consultations (consultation_date, quantity) VALUES (?, ?)', (date, quantity))
    connection.commit()
    connection.close()
    
def add_solar_installation(date, quantity):
    
    cur.execute('INSERT INTO SolarPanelInstallations (installation_date, quantity) VALUES (?, ?)', (date, quantity))
    connection.commit()
    connection.close()



def viewConsultations():

    # Fetch consultation bookings
    cur.execute('SELECT * FROM Consultations')

    
    return cur.fetchall()

def viewInstallations():
    
    # Fetch installation bookings
    cur.execute('SELECT * FROM SolarPanelInstallations')

    
    return cur.fetchall()

