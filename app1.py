from flask import Flask, app, json, render_template, request,jsonify
from keras.models import load_model
import numpy as np
app = Flask(__name__)

model = load_model('m.h5')

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    text=float(text)
    result=model.predict([text]).tolist()
    return json.dumps(result)
    

if __name__=='__main__':
    #app.debug=True
    app.run(debug= True)