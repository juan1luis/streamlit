import streamlit as st 
import pandas as pd


DATA_URL = 'https://raw.githubusercontent.com/juan1luis/streamlit/master/dataset.csv'

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

@st.cache
def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL)
    filtered_data_bysex = data[data['sex'] == sex]
    return filtered_data_bysex


data = load_data()
selectec_sex = st.selectbox('Select sex: ', data['sex'].unique())
btnFilterbySex = st.button('Filter by sex')

if (btnFilterbySex):
    filterbysex = load_data_bysex(selectec_sex)
    countrow = filterbysex.shape[0]
    st.write(f'Total sex: {countrow}')

    st.dataframe(filterbysex)