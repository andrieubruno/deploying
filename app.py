from flask import Flask, render_template, Response, request
import datetime, time
import os, sys
from threading import Thread

# def create_app(config):
create_app = Flask(__name__, template_folder='./templates')
    # app.config.from_object(config)

@create_app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    create_app.run(debug=True)
