from flask import Flask,redirect,render_template,request , url_for
from werkzeug.security import generate_password_hash,check_password_hash
import psycopg2 
from pgfunc import adduser , login_user , verify_password , hash_password ,get_db_connection
import bcrypt



conn = psycopg2.connect("dbname=home-ify user=postgres password=12345")
cur = conn.cursor()
 


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("forms.html")


@app.route("/landing")
def landing():
    return render_template("landing.html")

# @app.route("/signup" , methods=["POST","GET"])
# def adduser():
#     if request.method == 'POST':
#         fullname= request.form ['fullname']
#         password= request.form['password']
#         email= request.form['email']
#         new_user=(fullname,email,password)
#         adduser(new_user)
#         print(fullname)
#         print(password)
#         print(email)
#     return redirect("/")


# @app.route("/signup", methods=["POST", "GET"])
# def signup():
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         email = request.form['email']
#         password = request.form['password']    # Hash the password
        
#         if adduser(fullname, email, password):
#             print(f"User {fullname} added successfully.")
#         else:
#             print(f"Failed to add user {fullname}.")
        
#         return redirect("/")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        
        if adduser(fullname, email, password):
            print(f"User {fullname} added successfully.")
        else:
            print(f"Failed to add user {fullname}.")
        
        return redirect("/")
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        users = login_user()
        if not users:
            return "Error connecting to the database or fetching users"
        
        for user_email, user_password in users:
            if email == user_email and verify_password(user_password, password):
                return redirect(url_for('landing'))
        return "Invalid email or password"
    
    # return render_template("dummylanding.html")
   



if __name__ == '__main__':
    app.run(debug=True)
