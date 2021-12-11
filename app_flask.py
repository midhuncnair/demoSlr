import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

# os.chdir('D:\\ssridhar\\research\\AnalyticsBigdataML\\ML Course\\GreatLearning\\MTech-Weekend ML-1\\Session 8\\demo_slr')
print(os.getcwd())

# an object of WSGI application
from flask import Flask
app = Flask(__name__) # Flask constructor


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import slr_model

app = Flask(__name__)
model = pickle.load(open('demo_slr.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('demo_slr.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("here")
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('demo_slr.html', prediction_text='yhat:{}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
