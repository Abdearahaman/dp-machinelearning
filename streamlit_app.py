import streamlit as st
import pandas as pd

st.title('🤖Mchine learning App')

st.info('this app is building a machine learning app')

df = read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
df
