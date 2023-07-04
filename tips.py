import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
st.write("""
# Анализ чаевых ресторана
""")

st.write(""" 
Гистограмма total_bill
""")
fig,ax = plt.subplots()
sns.histplot(data=tips, x='total_bill', bins=10)
st.pyplot(fig)


st.write("""
Scatterplot, показывающий связь между total_bill and tip
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip')
st.pyplot(fig)


st.write("""
График, связывающий total_bill, tip, и size
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size')
st.pyplot(fig)



st.write("""
Связь между днем недели и размером счета
""")

fig,ax=plt.subplots()
sns.relplot(data=tips, x="day", y="total_bill")
st.pyplot(fig)


st.write("""
Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу
""")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='tip', y='day', hue='sex')
st.pyplot(fig)


st.write("""
Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)
""")

fig,ax=plt.subplots()
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
st.pyplot(fig)