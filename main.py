import streamlit as st
from home import home
from overview import overview
from insights import insight
from references import ref
st.set_page_config(layout='wide')
st.title('INFO-I 590: Data Visualization')
st.sidebar.title('Navigation')
pg=st.sidebar.radio("Go To",('Home','Overview','Insights','References'))

if pg=='Home':
    home()
elif pg=='Overview':
    overview()
elif pg=='Insights':
    insight()
elif pg=='References':
    ref()