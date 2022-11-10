import streamlit as st 
import pandas as pd


DATA_URL = 'https://raw.githubusercontent.com/juan1luis/streamlit/master/dataset.csv'



@st.cache
def load_data_byrange(startid,endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byname = data[(data['index'] >= startid) & (data['index']<endid)]

    return filtered_data_byname

startid = int(st.text_input('Start index: '))
endid = int(st.text_input('End index'))
btnRange = st.button('Search by range')


if (btnRange):
    filterbyrange = load_data_byrange(startid,endid)
    countrow = filterbyrange.shape[0]
    st.write(f'Total items: {countrow}')

    st.dataframe(filterbyrange)
    