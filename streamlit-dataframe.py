import streamlit as st
import pandas as pd

st.title('Dataframes')

names_link = 'dataset.csv'

names_data = pd.read_csv(names_link)

st.dataframe(names_data)
