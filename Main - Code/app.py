from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

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
        

        user = db.createUser(username, email, password) #Calls the DB Create function from the DB file

        

        return render_template("login.html") #Renders login page to allow user to login
    else:
        return render_template("signup.html")
    





    
@app.route("/login") #Login Page
def login():
    
    return render_template("login.html")

@app.route("/CCF") #Calculate Carbon Footprint [Client Requirement]
def CCF():

    return render_template("CCF.html")

@app.route("/EP") #Energy Products [Client Requirement]
def EP():

    return render_template("EP.html")

@app.route("/HTRCF") #How to reduce your carbon footprint [Client Requirement]
def HTRCF():

    return render_template("HTRCF.html")

@app.route("/about") #aboutUs Page
def aboutUs():

    return render_template("aboutUS.html")

@app.route("/support") #Support page
def support():

    return render_template("support.html")

@app.route("/legal") #Legal Page/legal Requirements page
def legal():

    return render_template("legal.html")

@app.route("/PP") #Privacy Policy page
def privacyPolicy():

    return render_template("pp.html")



if __name__ == "__main__":
    app.run(debug=True)