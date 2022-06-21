# Basic flask web app
from flask import Flask, render_template, request, redirect, url_for

# Create a flask app
app = Flask(__name__)

# Define the route for the default web page
@app.route('/')
def home():
    return "Hello World!"
# Define the route for the about page
@app.route('/about')
def about():
    return "About page"

