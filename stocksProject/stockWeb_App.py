#This is a Stocks Web Appliction
#Importing Libraries
from datetime import datetime
from typing import Union
import streamlit as st
import pandas as pd
from PIL import Image
from pandas import DatetimeIndex, Series
from pandas._libs.tslibs.nattype import NaTType
#Add Title And Image
st.write("""
# Stock Market Web Application
**Visually** show data on a stock! 
""")

image = Image.open("C:/Users/Vishal/Desktop/stocksProject/pro/icon.jpg")
st.image(image, use_column_width= True)
#create sidebar header
st.sidebar.header('User Input')
#creating function to get user input
def get_input():
    start_date= st.sidebar.text_input("Start Date", "01-01-2018")
    end_date= st.sidebar.text_input("End Date", "01-01-2021")
    stock_symbol= st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol
#creating function to get company name
def get_comp_name(symbol):
    if symbol == "AMZN":
        return 'Amazon'
    elif symbol == "TSLA":
        return 'Tesla'
    elif symbol == "GOOG":
        return 'Google'
    else:
        'None'
#creating fuction to get proper company data and proper time frame from the user start date to the users end date
def get_data(symbol, start, end):
#Load Data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("C:/Users/Vishal/Desktop/stocksProject/csv/AMZN.csv")
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("C:/Users/Vishal/Desktop/stocksProject/csv/TSLA.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("C:/Users/Vishal/Desktop/stocksProject/csv/GOOG.csv")
    else:
        df = pd.DataFrame(columns= ['Date', 'Close', 'Open', 'Volume', 'Adj close', 'High', 'Low'])
#get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
#Sent the start and end index row both to 0
    start_row = 0
    end_row = 0

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i] ):
            start_row = i
            break

    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'] [len(df)-1-j] ):
            end_row = len(df) -1 -j
            break
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row +1, :]

start, end, symbol = get_input()

df = get_data(symbol, start, end)

company_name = get_comp_name(symbol.upper())


st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])


st.header('Data Statistics')
st.write(df.describe())








