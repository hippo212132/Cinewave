from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import datetime

import db



app = Flask(__name__)


app.config["SESSION_TYPE"] = (
    "filesystem"
)

Session(app)



@app.route("/") #Website Landing Page
def index():

    if not session.get("user"): #Checking if there is a session avaliable

        return render_template("index.html") #If Session is not avaliable, render Logged-out Home page
    
    return render_template("index.html", user=session["user"]) #If Session is avaliable, Render Logged-in Home Page



@app.route("/signup", methods = ["GET", "POST"])
def signup():
    
    if session.get("user"):
        return render_template("index.html", user=session["user"])
    

    if request.method == "POST": #If Form method == POST then gather the inputted fields

        
        username = request.form.get("username")

        if len(username) <= 0 >= 16:
            return render_template("signup.html", error="Username must be between 1-16 characters")
        
        if not str(username):
            return render_template("signup.html", error="No numbers or special characters allowed")
        
        
        
        
        
        
        email = request.form.get("email")

        

        if ".com" not in email or "gmail"  and "@" not in email:

            return render_template("signup.html", error="Please enter a valid email")
        
        
        password = request.form.get("password")
        if len(password) < 8:
            return render_template("signup.html", error="Please Enter a Valid password")
       
        
        cpass = request.form.get("cpass")
        
        if cpass != password:
            return render_template("signup.html", error="Please make sure confirm password matches password")
        

        db.createUser(username, email, password) #Calls the DB Create function from the DB file

        

        return render_template("login.html") #Renders login page to allow user to login
    else:
        return render_template("signup.html")
    





    
@app.route("/login", methods=["GET", "POST"]) #Login Page
def login():

    if session.get("user"):
        return render_template("index.html", user=session["user"])
    

    if request.method == "POST":
    
        email = request.form.get("email")
        #Email Validation
        if len(email) <= 0:
            return render_template("login.html", error="Please enter a valid EMAIL")
        
        symbol = "@"
        domain = ".com"
        specialChar1 = "!"

        if symbol not in email and domain not in email:
            return render_template("login.html", error="An email must contain one @ Symbol")
        #~~~~~~~~~~~~~~


        password = request.form.get("password")
        #Password Validation not required since all it has to do is match the database
        
        

        user = db.checkUser(email, password)

        session["user"] = user

        return render_template("index.html", user=session["user"])
    else:
        return render_template("login.html")

@app.route("/book", methods=["POST", "GET"])
def booking():
    if not session.get("user"):
        return render_template("signup.html")
    
    if request.method == 'POST':
        booking_type = request.form.get("booking_type")

        time = request.form.get("time")

        dateTime = datetime.datetime.now()
        if time < str(dateTime.time()):
            return render_template("booking.html", error="You cannot enter a past time")

        date = request.form.get("date")
        if date < str(datetime.date.today()):
            return render_template("booking.html", error="You cannot enter a past date")
        quantity = request.form.get("quantity")

        if booking_type == 'regTicket':
            db.book_ticket(date, time, quantity)
            return redirect(url_for('index'))
        
        elif booking_type == 'premTicket':
            db.book_ticket(date, time, quantity)
            return redirect(url_for('index'))

    return render_template('booking.html', user=session["user"])

@app.route("/logout")
def logout():
    if session.get("user"):
        session.clear()

        return render_template("index.html")

@app.route('/view')
def viewBookings():
    
    Tickets = db.viewTicket()
    
    return render_template('viewbookings.html', user=session["user"], Tickets=Tickets)

@app.route("/CCF") #Calculate Carbon Footprint [Client Requirement]
def CCF():

    if session.get("user"):
        return render_template("CCF.html", user=session["user"])

    return render_template("CCF.html")

@app.route("/account", methods=["POST", "GET"])
def account():

    if not session.get("user"):
        return render_template("index.html")
    

    
    if request.method == "POST":
        
        type = request.form.get("2fa")
        enable = request.form.get("Enable")
        disable = request.form.get("Disable")

        if type == enable:
            db.twoFactorEnabled()

        elif type == disable:
            db.twoFactorDisabled()
    
    return render_template("account.html", user=session["user"])
        

@app.route("/EP") #Energy Products [Client Requirement]
def EP():

    if session.get("user"):
        return render_template("EP.html", user=session["user"])


    return render_template("EP.html")

@app.route("/HTRCF") #How to reduce your carbon footprint [Client Requirement]
def HTRCF():

    if session.get("user"):
        return render_template("HTRCF.html", user=session["user"])


    return render_template("HTRCF.html")

@app.route("/about") #aboutUs Page
def aboutUs():

    if session.get("user"):
        return render_template("aboutUS.html", user=session["user"])


    return render_template("aboutUS.html")

@app.route("/support") #Support page
def support():

    if session.get("user"):
        return render_template("support.html", user=session["user"])


    return render_template("support.html")

@app.route("/legal") #Legal Page/legal Requirements page
def legal():

    if session.get("user"):
        return render_template("legal.html", user=session["user"])
    

    return render_template("legal.html")

@app.route("/PP") #Privacy Policy page
def privacyPolicy():

    if session.get("user"):
        return render_template("pp.html", user=session["user"])


    return render_template("pp.html")



if __name__ == "__main__":
    app.run(debug=True)