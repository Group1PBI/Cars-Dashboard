import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
df = pd.read_csv('Cars data.csv')
tab = st.radio('Select Section',['Cover','KPI','Charts'])
if tab != 'Cover':
    d7 = ['all']+df['Manufacturer'].unique().tolist()
    d8 = ['all']+df['transmission'].unique().tolist()
    d9 = ['all']+df['fuelType'].unique().tolist()
    st.sidebar.title('Filters')
    A = st.sidebar.selectbox(label='Manufacturer',options=d7)
    B = st.sidebar.selectbox(label='Transmission',options=d8)
    C = st.sidebar.selectbox(label='Fuel Type',options=d9)
    if A != 'all':
        df = df[df['Manufacturer']==A]
    if B != 'all':
        df = df[df['transmission']==B]
    if C != 'all':
        df = df[df['fuelType']==C]

if tab == 'Cover':
    st.image('download.jpg')
    st.title('Cars Features Dashboard')
elif tab == 'KPI':
    No_OF_Cars = f"{np.round(df['model'].count()/1000,0)}K"
    st.metric(label='No of Cars',value=No_OF_Cars)
    Avg_Cars_Price =f"{np.round(df['price'].mean()/1000,2)}K"
    st.metric(label='Avg. Cars Price',value=Avg_Cars_Price)
    Taxes = f"{np.round(df['tax'].sum()/1000000,2)}M"
    st.metric(label='Taxes',value=Taxes)
    max_mpg = df['mpg'].max()
    fil_mpg = df[df['mpg']==max_mpg]
    min_price = fil_mpg['price'].min()
    fil_pr = fil_mpg[fil_mpg['price']==min_price]
    The_Most_Fuel_Efficient_Car = fil_pr['model'].iloc[0]
    st.metric(label='The Most Fuel Efficient Car',value=str(The_Most_Fuel_Efficient_Car))
elif tab == 'Charts':
    col1,col2 = st.columns(2)
    with col1:
        d3 = df.groupby('engineSize')['price'].mean().reset_index()
        fig3 = px.line(d3,x='engineSize',y='price',title='Avg. Price by Engine Size')
        st.plotly_chart(fig3)
        d5 = df.groupby('year')['model'].count().reset_index()
        fig5 = px.line(d5,x='year',y='model',title='Yearly Car Distribution')
        st.plotly_chart(fig5)
        
        d2 = df.groupby('transmission')['model'].count().reset_index().sort_values('model',ascending=False)
        fig2 = px.pie(d2,names='transmission',values='model',title='No of cars by Transmission',hole=.6)
        st.plotly_chart(fig2)
        
    with col2:
        d4 = df.groupby('mileage')['price'].mean().reset_index()
        fig4 = px.line(d4,x='mileage',y='price',title='Avg. Price by MileAge')
        st.plotly_chart(fig4)
        d1 = df.groupby('Manufacturer')['price'].sum().reset_index().sort_values(by='price',ascending=False)
        fig1 = px.bar(d1,x='Manufacturer',y='price',title='Price by Manufacturer',text_auto='.2s')
        st.plotly_chart(fig1)
        