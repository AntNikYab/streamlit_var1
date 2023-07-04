import yfinance as yf
import streamlit as st

st.write("""
# Приложение стоимости акций

цена закрытия акций Tesla и объем торгов

""")
         
tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d', start='2013-09-01', end='2023-07-03')

st.write('''
## Цена закрытия
''')
st.line_chart(tickerDF.Close)
st.write('''
## Объем торгов
''')
st.line_chart(tickerDF.Volume)