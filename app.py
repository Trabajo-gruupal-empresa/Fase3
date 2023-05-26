from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secretkey = 'mysecretkey'
print (DATABASE_ADDRESS)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_ADDRESS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 