# Creating app.py, naming is important
# Let's see how we can use Python Flask to interact with our browser

from flask import Flask, redirect, url_for, render_template  # installed via pip method

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
    return render_template("welcome.html") # redirects to .html file

# Let's create a decorator to route traffic to login page
# Display 2 messages of your choice in form of h1 and h2
# What if a page is unavailable? I want to be able to control this
# flask contains redirect and url_for for this

@app.route("/login/")
def login():
    return redirect(url_for("welcome")) # redirects to welcome page
           #"<h1> Welcome to the login page.</h1>" \
           #"<h2> Please enter your login details below:</h2>"

if __name__ == "__main__":
    app.run(debug=True)

# Let's add out HTML file to redirect from Python flask to .html file
# Create a folder called templates
# project folder
#    templates folder
#       welcome.html file
#    app.py
