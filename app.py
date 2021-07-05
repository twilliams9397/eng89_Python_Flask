# Creating app.py, naming is important
# Let's see how we can use Python Flask to interact with our browser

from flask import Flask  # installed via pip method

# We have to create an object of this class
app = Flask(__name__)  # creating app instance

# Let's create a function to link to our home/default page, and connect it to our browser
@app.route("/") # decorating our function with @app.route to set route in browser
def index():
    return "Welcome to Engineering 89 DevOps team."

# flask run in terminal to run

# Let's create a welcome page
@app.route("/welcome/") # / at end will work if it isnt typed in browser - /welcome
def welcome():
    return "<h1> Welcome page for Flask app.</h1>"

# Let's create a decorator to route traffic to login page
# Display 2 messages of your choice in form of h1 and h2

@app.route("/login/")
def login():
    return "<h1> Welcome to the login page.</h1>" \
           "<h2> Please enter your login details below:</h2>"
