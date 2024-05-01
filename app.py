from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

model = load_model('your_model.h5')  # Load the TensorFlow model

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        present_price = float(request.form['price'])
        car_age = int(request.form['age'])
        seller_type = 1 if request.form['seller'] == 'Individual' else 0
        fuel_type = 1 if request.form['fuel'] == 'Diesel' else 0
        transmission_type = 1 if request.form['transmission'] == 'Manual' else 0

        # Prepare input data for prediction
        input_data = np.array([[present_price, car_age, fuel_type, seller_type, transmission_type]])

        # Make prediction
        prediction = model.predict(input_data)
        output = round(prediction[0][0], 2)

        return render_template('index.html', output="{} Lakh".format(output))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
