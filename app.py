#python3 -m venv env
#source env/bin/activate
#pip3 install flask
#pip3 install scikit-learn
#pip3 install pandas
#pip3 install gunicorn
#pip3 list 
#pip3 freeze>requirements.txt
#flask run --debug

#deactivate   
#pip install -r requirements.txt

import numpy as np

from flask import Flask,request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb")) #read binary

@app.route("/")
def home():
    return render_template("index.html")

## submit route'u
@app.route("/predict", methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array([int_features])
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template("index.html", text = f"Salary {output} TL")

