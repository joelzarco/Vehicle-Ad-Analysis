# Vehicles ads Analysis
import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')
# 
hist_button = st.button('First Histogram') 
if hist_button: # al hacer clic en el botón
    st.write('Milage is mostly concentrated in cars with less than 200k miles and excelent conditions')    
    odo_vs_price = px.scatter(car_data, x=car_data.odometer, y=car_data.price, color=car_data.condition, title='Odometer vs Price sale')
    st.plotly_chart(odo_vs_price, use_container_width=True)