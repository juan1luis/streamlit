import streamlit as st
import pandas as pd

st.title('Dataframes')

DATA_URL = 'https://raw.githubusercontent.com/juan1luis/streamlit/master/dataset.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    return data

data_load_state = st.text('Loading data...')

data = load_data(1000)

data_load_state.text('Done! (using st.cache)')

st.dataframe(data)