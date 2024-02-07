import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
model1 = pickle.load(open('sw (1).pkl', 'rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index') # rendering the html template
def index() :
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    brand = int(request.form['Brand'])
    model = int(request.form['Model'])
    os = int(request.form['Operating_System'])
    connect = int(request.form[ 'Connectivity'])
    resolution = int(request.form['Resolution'])
    display_type = int(request.form['Display Type'])
    heart_rate = int(request.form['Heart_Rate_Monitor'])
    gps = int(request.form['GPS'])
    nfc = int(request.form['NFC'])
    water = int(request.form['Water_Resistance_meters'])
    battery =int(request.form['Battery_Life_days'])
    display_size = float(request.form['Display_Size_inches'])
    prediction = model1.predict(pd.DataFrame([[brand,model,os,connect,display_type,display_size,resolution,water,battery,heart_rate,gps,nfc]],
                                            columns=['Brand','Model','Operating System','Connectivity',
                                                    'Display Type','Display Size','Resolution',
                                                    'Water Resistance','Battery Life','Heart Rate Monitor',
                                                    'GPS','NFC']))
    prediction = np.round(prediction,2)
    return  render_template('index.html' ,prediction_text= "is {}".format(prediction))

if __name__ == '__main__':
    app.run(debug=True)