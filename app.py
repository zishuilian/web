from flask import Flask, request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import flash, redirect, url_for

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'  # for example, '3ef6ffg4'


@app.route('/home', methods=['get', 'post'])
@app.route('/', methods=['get', 'post'])
def home():
    return app.send_static_file('login.html')


@app.route('/table.html', methods=['get', 'post'])
def login():
    return app.send_static_file('table.html')


@app.route('/tab', methods=['get', 'post'])
def log():
    return app.send_static_file('table.html')


@app.route('/blank', methods=['get', 'post'])
def blank():
    return app.send_static_file('blank.html')


if __name__ == '__main__':
    app.run(port=80)
