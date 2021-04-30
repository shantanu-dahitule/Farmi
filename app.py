"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
model = pickle.load(open('farmi.pkl', 'rb'))
label=pickle.load(open('labelencoder.pkl','rb'))
dict =pickle.load(open('dict.pkl','rb'))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql:////blog.sql"
db = SQLAlchemy(app)
 
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
@app.route('/')
# welcome page
def Welcome():
    return render_template("Welcome.html")

@app.route('/home')
# Home page 
def home():       
    return render_template("/index.html")
@app.route('/predict', methods=['POST'])
def predict():
    #preiction_backend  
    int_features =[[float(x) for x in request.form.values()]] 
    prediction = model.predict(int_features)
    output = int(round(prediction[0], 0)) 
    dict2 = {0: 'rice', 1: 'maize', 2: 'chickpea', 3: 'kidneybeans', 4: 'pigeonpeas', 5: 'mothbeans', 6: 'mungbean', 7: 'blackgram', 8: 'lentil', 9: 'pomegranate', 10: 'banana', 11: 'mango', 12: 'grapes', 13: 'watermelon', 14: 'muskmelon', 15: 'apple', 16: 'orange', 17: 'papaya', 18: 'coconut', 19: 'cotton', 20: 'jute', 21: 'coffee'}
    if output>21:
        output=output-21
    else:
        pass
    predictionIs = dict[output]
    return render_template('index.html', prediction='You can take : {} and {}'.format(predictionIs, dict2[output]))
@app.route('/about')
# About page
def about():
    return render_template("/about.html")

@app.route('/blog')
# Blog page  
def blog ():   

    return render_template("/blog.html")
@app.route('/contact')
#contact page
def Contact():
    return render_template("/contact.html")






if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)