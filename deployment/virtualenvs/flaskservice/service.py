from flask import Flask, jsonify, request, render_template
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

app = Flask(__name__)

toxic_model = pickle.load(open('./pickles/tvec_lr.sav', 'rb'))
label_model = pickle.load(open('./pickles/cvec_clflr.sav', 'rb'))
label_list = ['Obscene','Insult','Identity Attack','Others']

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict-comment-interface', methods = ["GET", "POST"])
def predict_comment_interface():

    output = None

    if request.method == "POST":
        comment = request.form["comment"]
        output = toxic_model.predict([comment])[0]
        if output != 1:
        	output = "This comment is clean!"
        else:
        	label_str = []
        	label = label_model.predict([comment])[0]
        	for i in range(len(label)):
        		if label[i] == 1:
        			label_str.append(label_list[i])
        	output = "This comment is toxic! Toxic Labels: " + ",".join(label_str)

        		

    return render_template("base.html", output = output)