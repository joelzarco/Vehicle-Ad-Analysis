# Vehicles ads Analysis
import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Ad Car sales Visual Analysis for the US market')

# milage vs price
scatter_button = st.button('Mileage vs Price') 
if scatter_button: # al hacer clic en el botón
    st.write('Mileage is mostly concentrated in cars with less than 200k miles')    
    odo_vs_price = px.scatter(car_data, x=car_data.odometer, y=car_data.price, color=car_data.condition, title='Odometer vs Price sale')
    st.plotly_chart(odo_vs_price, use_container_width=True)

# median price sale
boxplot_button = st.button('Median price per condition')
if boxplot_button:
	st.write('Median price for all categories is close to 12k USD, for New cars average sale price is close to 22k USD')
	price_boxplot = px.box(car_data, x=car_data.condition, y=car_data.price, title='Average car price')
	st.plotly_chart(price_boxplot, use_container_width=True)
	#price_boxplot.show()

# Histogram
hist_button = st.button('Price distribution among categories')
if hist_button:
	st.write('Fair and Excelent conditions control a great percentaje of ad listings')
	price_hist = px.histogram(car_data, x=car_data.price, color=car_data.condition, title='Price distribution per category')
	st.plotly_chart(price_hist, use_container_width=True)

# sub-dataset
not_automatic = car_data[car_data.transmission != 'automatic']
# check boxes
auto_checkbox = st.checkbox('Automatic Vs Manual transmission')
if auto_checkbox:
	#
	not_auto_hist = px.histogram(not_automatic, x=not_automatic.condition, color=not_automatic.transmission, title='Condition vs Manual Transmission')
	st.plotly_chart(not_auto_hist, use_container_width=True)
else:
	all_trans_hist = px.histogram(car_data, x=car_data.condition, color=car_data.transmission, title='Condition vs All Transmissions')
	st.plotly_chart(all_trans_hist, use_container_width=True)

