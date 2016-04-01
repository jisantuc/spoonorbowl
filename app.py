import random
import os
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    images = os.listdir('static/images')
    image = random.choice(images)
    return render_template(
        'index.html',
        image=image
    )

@app.route('/process', methods=['POST'])
def process():
    ''' records votes and redirects to another image '''
    pass 
