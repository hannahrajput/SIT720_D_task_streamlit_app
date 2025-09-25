import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load("house_price_model.pkl")


st.title("Melbourne House Price Prediction")
st.write("Enter the details of the property to predict its price:")

st.sidebar.header("Property Features")


suburb = st.sidebar.selectbox("Suburb", ["Abbotsford", "South Yarra", "Brighton"])
rooms = st.sidebar.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
type_property = st.sidebar.selectbox("Type (h = house, u = unit, t = townhouse)", ["h", "u", "t"])
distance = st.sidebar.number_input("Distance from CBD (km)", min_value=0.0, max_value=20.0, value=5.0)
bedroom2 = st.sidebar.number_input("Number of Bedrooms", min_value=0, max_value=10, value=3)
bathroom = st.sidebar.number_input("Number of Bathrooms", min_value=0, max_value=10, value=2)
car = st.sidebar.number_input("Number of Car Spaces", min_value=0, max_value=10, value=1)
landsize = st.sidebar.number_input("Land Size (sqm)", min_value=0, max_value=20000, value=200)
buildingarea = st.sidebar.number_input("Building Area (sqm)", min_value=0, max_value=1000, value=150)
yearbuilt = st.sidebar.number_input("Year Built", min_value=1800, max_value=2025, value=1990)
schools_nearby = st.sidebar.number_input("Number of Schools Nearby", min_value=0, max_value=20, value=3)
sale_date = st.sidebar.date_input("Sale Date")  
year_sold = sale_date.year
month_sold = sale_date.month
day_sold = sale_date.day

input_data = {
    "Rooms": [rooms],
    "Bedroom2": [bedroom2],
    "Bathroom": [bathroom],
    "Car": [car],
    "Landsize": [landsize],
    "BuildingArea": [buildingarea],
    "YearBuilt": [yearbuilt],
    "Distance": [distance],
    "Suburb": [suburb],  
    "Address": ["dummy"],      
    "Type": [type_property],             
    "Method": ["S"],           
    "SellerG": ["Biggin"],     
    "Date": ["01/01/2016"],    
    "Postcode": [3067],        
    "CouncilArea": ["Yarra City Council"],  
    "Lattitude": [-37.8],                  
    "Longtitude": [145.0],                 
    "Regionname": ["Northern Metropolitan"], 
    "Propertycount": [4000],
    "SchoolsNearby": [schools_nearby],
    "YearSold": [year_sold],                 
    "MonthSold": [month_sold],                  
    "DaySold": [day_sold]  
}

input_df = pd.DataFrame(input_data)

if st.button("Predict Price"):
    try:
        prediction = model.predict(input_df)
        st.success(f"Estimated House Price: ${prediction[0]:,.0f}")
    except Exception as e:
        st.error(f"Error: {e}")
