from datetime import datetime
import streamlit as st
import requests
import config
from iex import Stock

symbol = st.sidebar.text_input('Symbol')

stock = Stock(config.IEX_API_KEY,symbol)
view = st.sidebar.selectbox('View',{'Overview','Fundamental','News','Onwership','Technicals'})
st.title(view)

if view == 'Overview':
    logo = stock.get_logo()
    company_info = stock.get_company_info()
    #previous = stock.get_previous()
    
    col1,col2 = st.columns(2)

    with col1:
        st.image(logo['url'])
        st.header(company_info['companyName'])
        st.subheader('Industry')
        st.write(company_info['industry'])
        st.subheader('Sector')
        st.write(company_info['sector'])
        
        
    with col2:
        st.subheader('Description')
        st.write(company_info['description'])

    
if view == 'Fundamental':
    pass
    
if view == 'News':
    last = 10
    news = stock.get_news(last)
    
 
    for x in range(last):
        st.subheader(news[x]['headline'])
        col1,col2 = st.columns(2)
        with col1:
            st.write( datetime.fromtimestamp(int(news[x]['datetime']) / 1e3))
        st.image(news[x]['image'])
        st.write(news[x]['summary'])   
        col1,col2 = st.columns(2)
        with col1:
            st.write('**related stock:**')  
        with col2:     
            st.write(news[x]['related'])  
            
        col1,col2 = st.columns(2)
        with col1:
            st.write('**URL:**')
        with col2:
            st.write(news[x]['url'])
            
if view == 'Onwership':
    pass
if view == 'Technicals':
    pass