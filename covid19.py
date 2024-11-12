
import pandas as pd 
import streamlit as st
import numpy as np 
#importlib.import_module('numpy')
#import matplotlib.pyplot as plt  
dataset=pd.read_csv('c:/Users/user/Desktop/Application/naija_data.csv')
#st.data_editor(dataset)
st.title('Covid 19 Pandemic Distribution in Nigeria')

st.header("States Data Distribution")
#page=st.sidebar.selectbox("About Pandamic Analysis",("Display information","Covid 19 Analysis","Total"))
#if page=="Display information":
if st.button("Show Distribution"):
        st.write(dataset)
#if page=="Covid 19 Analysis":
if st.button("Analyze"):
         st.write(dataset.describe())
#if page=="Total":
if st.button("Sum of Cases"):
        st.write("Total number of confirmed cases: ",dataset['confirmed_cases'].sum())
        st.write("Total number of deaths : ",dataset['deaths'].sum())
        st.write("Active cases: ",dataset["active_cases"].sum())
        st.write('Total discharged cases: ',dataset['discharged'].sum())
st.header("Visualize ")
if st.button("Bar chart"):
        st.bar_chart(dataset[['deaths',"confirmed_cases"]], x="deaths",y="confirmed_cases")
if st.button('Line Chart'):
        st.line_chart(dataset['deaths'])
#data=fetchdata()
#st.map(data)
        
        
    