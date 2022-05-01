
   
from flask import Flask, render_template, request
import numpy as np
import pickle


# https://youtu.be/pMIwu5FwJ78

model = pickle.load(open("model (1).pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method=="POST":
        input_dict = request.form.to_dict()
        input_values = list(input_dict.values())
        print(input_values)
        if input_values[0]=="on":
            input_values[0]=1
        else:
            input_values[0]=0
        input_values = list(map(float, list(input_values)))
        print(input_values)
        input_values = np.array(input_values)
        input_values = input_values.reshape(1, -1)
        prediction = model.predict(input_values)[0]
        message = ""
        if prediction==0:
            message="Patient is not COVID"
        else:
            message="Patient is COVID"
        return message
        
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')