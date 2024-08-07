import streamlit as st
import pandas as pd

st.title('🤖Mchine learning App')

st.info('this app is building a machine learning app')
with st.expander('Data'):
  st.write("**Raw data:**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df
