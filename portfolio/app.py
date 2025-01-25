from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')