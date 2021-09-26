from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts
from mail import *

app = Flask(__name__)

CORS(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        send_email(name, email, "message.txt")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)