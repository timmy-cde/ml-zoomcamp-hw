import pickle

from flask import Flask
from flask import request
from flask import jsonify

with open('model1.bin', 'rb') as f_in_model:
    model = pickle.load(f_in_model)

with open('dv.bin', 'rb') as f_in_dv:
    dv = pickle.load(f_in_dv)


# Q3
# ----------------------------------------------------------------------
# customer = {"job": "management", "duration": 400, "poutcome": "success"}

# X = dv.transform([customer])
# y_pred = model.predict_proba(X)[0, 1]

# print(y_pred)   # answer: 0.7590966516879658
# ----------------------------------------------------------------------

# Q4 ~ Q6
# ----------------------------------------------------------------------
app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'churn_probability': float(y_pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
