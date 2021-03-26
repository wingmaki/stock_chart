#2021-03-26
import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

start = st.text_input('開始日')
end = st.text_input('終了日')
input_code = st.text_input('銘柄コード')
code = input_code + '.jp'



if not start or not end or not code:
    st.write('入力してね')
else:
    
    df = data.DataReader(code ,'stooq', start, end)
    date = df.index
    price = df['Close']
    
    fig = plt.figure(figsize=(30,10))
    plt.plot(date,price,)
    #fig = plt.plot(date,price,label='Close')
    st.pyplot(fig)
    #st.write(price)
    
    
    