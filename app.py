import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Котировки компании Apple 🍏

Ну что ж, посмотрим, нужно ли нам покупать акции или нет, ***let's go***!

""")

start_date = st.sidebar.date_input('Дата начала', value=pd.to_datetime('2023-01-01'))
end_date = st.sidebar.date_input('Дата окончания', value=pd.to_datetime('today'))

data = yf.download('AAPL', start=start_date, end=end_date)

if not data.empty:
    '''
    ***График цены закрытия***
    '''
    st.line_chart(data['Close'], width=0, height=0, use_container_width=True)
    '''
    ***График объёма торгов***
    '''
    st.line_chart(data['Volume'], width=0, height=0, use_container_width=True)
else:
    st.write('Измените даты :)')
