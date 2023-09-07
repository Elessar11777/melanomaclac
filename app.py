from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('./CoxPHFitter_most_basic_on_cells_df.pickle', 'rb') as file:
    cph = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the values from the form
    l1 = request.form['l1']
    l2 = request.form['l2']
    l3 = request.form['l3']
    t1 = request.form['t1']
    n1 = request.form['n1']
    p1 = request.form['p1']
    m1 = request.form['m1']
    e1 = request.form['e1']

    # Convert the values to an array
    row_to_predict = np.array([l1, l2, l3, t1, n1, p1, m1, e1])

    # Make the prediction
    survival_predict = cph.predict_expectation(np.transpose(row_to_predict))
    survival_month = (survival_predict.unique()[0] / 30.44)
    int_month = int(survival_month)
    fractional_part = survival_month - int_month
    days = round(fractional_part * 30.44)


    int_month = str(int_month)
    days = str(days)
    return render_template('index.html', prediction_month=int_month, prediction_days=days)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
