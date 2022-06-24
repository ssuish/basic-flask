# Basic flask web app
from flask import Flask, render_template, request, redirect, url_for
import src.post

# Create a flask app
app = Flask(__name__)

# Define the route for the default web page
@app.route('/')
def home():
    return render_template('index.html') # return to html file.

@app.route('/about')
def about():
    return render_template('about.html', posts=src.post.post_list, title="About Us")

if __name__ == '__main__':
    app.run(debug=True)