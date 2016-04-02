import random
import os
from flask import Flask, url_for, render_template, request
from dbsetup import Session, Vote

app = Flask(__name__)

def get_random_image():
    images = os.listdir('static/images')
    return random.choice(images)

@app.route('/')
@app.route('/index')
def index():
    image = get_random_image()
    return render_template(
        'index.html',
        image=image
    )

@app.route('/process', methods=['POST'])
def process():
    ''' records votes and redirects to another image '''

    formData = request.values
    vals = formData.to_dict()

    im, score = [(k, v) for k, v in vals.items()][0]
    added = Vote.add(im, score)

    image = get_random_image()

    return render_template(
        'index_sub.html',
        image=image,
        last_image=im,
        last_score=score,
        mean_score=added.mean(im)
    )

if __name__=="__main__":
	app.run(debug=True)
