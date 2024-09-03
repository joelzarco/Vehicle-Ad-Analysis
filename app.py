# Vehicles ads Analysis
import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

# milage vs price
scatter_button = st.button('Scatter Plot') 
if scatter_button: # al hacer clic en el botón
    st.write('Milage is mostly concentrated in cars with less than 200k miles')    
    odo_vs_price = px.scatter(car_data, x=car_data.odometer, y=car_data.price, color=car_data.condition, title='Odometer vs Price sale')
    st.plotly_chart(odo_vs_price, use_container_width=True)

# median price sale
boxplot_button = st.button('Median price per condition')
if boxplot_button:
	st.write('Median price for all categories is close to 12k USD, for New cars average sale price is close to 22k USD')
	price_boxplot = px.box(car_data, x=car_data.condition, y=car_data.price)
	st.plotly_chart(price_boxplot, use_container_width=True)
	#price_boxplot.show()
