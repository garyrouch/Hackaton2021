import requests
import pandas as pd
import numpy as np
import pickle
import flask
from flask import Flask, request
import json
from config import MODEL
pickle_path = MODEL

loaded_model = pickle.load(open(pickle_path, 'rb'))

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome, please input your features'

# @app.route('/predict_')
# def prediction():
#     inputs = request.args
#     inputs_list = list(inputs.values())
#     solution = loaded_model.predict_proba([inputs_list])
#     pred = []
#     for i in solution:
#         if i[1] > 0.65:
#             pred = 1
#         else:
#             pred = 0
#     return {'prediction': pred}

@app.route('/predict', methods=['POST'] )
def prediction():
    predict_data = json.loads(flask.request.get_json())
    predict_df = pd.DataFrame(predict_data)
    # inputs = request.args
    # inputs_list = list(inputs.values())
    solution = loaded_model.predict_proba(predict_df)
    for i in solution:
        if i[1] > 0.65:
            pred = 1
        else:
            pred = 0
    result = {'result': solution}
    return flask.jsonify(result)
    # return {'prediction': int(solution)}

if __name__ == '__main__':
    app.run()