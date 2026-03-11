import streamlit as st
import pandas as pd
import pickle

# load model
model = pickle.load(open("car_price_model.pkl", "rb"))

st.title("Used Car Price Prediction")

st.write("Enter Car Details")

# user inputs
car_age = st.number_input("Car Age")
fuel = st.selectbox("Fuel Type", ["Petrol","Diesel","CNG","LPG"])
transmission = st.selectbox("Transmission", ["Manual","Automatic"])
owner = st.selectbox("Owner Type", ["First Owner","Second Owner","Third Owner"])
km_driven = st.number_input("Kilometers Driven")

# convert inputs to numbers
fuel_dict = {"Petrol":1,"Diesel":0,"CNG":2,"LPG":3}
transmission_dict = {"Manual":1,"Automatic":0}
owner_dict = {"First Owner":0,"Second Owner":1,"Third Owner":2}

fuel = fuel_dict[fuel]
transmission = transmission_dict[transmission]
owner = owner_dict[owner]

# prediction
if st.button("Predict Price"):

    data = pd.DataFrame({
        'car_age':[car_age],
        'fuel':[fuel],
        'transmission':[transmission],
        'owner':[owner],
        'km_driven':[km_driven]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Car Price: ₹{int(prediction[0])}")
