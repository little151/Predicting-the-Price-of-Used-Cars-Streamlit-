import streamlit as st
import pickle
import random

# Load the model
try:
    model = pickle.load(open('used_car_price_prediction_model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please make sure the model file 'used_car_price_prediction_model.pkl' exists.")
    st.stop()

def predict_price(present_price, car_age, seller_type, fuel_type, transmission_type):
    # Convert categorical variables to numerical if needed
    fuel_type = 1 if fuel_type == 'Diesel' else 0
    seller_type = 1 if seller_type == 'Individual' else 0
    transmission_type = 1 if transmission_type == 'Manual' else 0

    # Perform prediction
    try:
        prediction = model.predict([[present_price, car_age, fuel_type, seller_type, transmission_type]])
        return round(prediction[0], 2)
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        return None

def generate_random_price(present_price):
    # Generate a random price within the specified range
    if present_price <= 10:
        min_price = 4
        max_price = 8
    else:
        min_price = max(0, present_price - 3)
        max_price = max(0, present_price - 10)
    return round(random.uniform(min_price, max_price), 2)

def main():
    st.title('Car Price Prediction')

    present_price = st.number_input('Enter the present price of the car (in Lakhs)')
    car_age = st.number_input('Enter the age of the car (in years)')

    seller_type = st.selectbox('Select seller type', ('Individual', 'Dealer'))
    fuel_type = st.selectbox('Select fuel type', ('Petrol', 'Diesel'))
    transmission_type = st.selectbox('Select transmission type', ('Manual', 'Automatic'))

    if st.button('Predict Price'):
        if present_price <= 10:
            st.error('Please enter a value greater than 10 for the present price')
        elif car_age == 0:
            st.error('Please insert the age for Enter the age of the car (in years)')
        else:
            random_price = generate_random_price(present_price)
            st.success(f'Randomly Generated Price: {random_price} Lakhs')

if __name__ == '__main__':
    main()
