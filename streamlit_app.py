import streamlit as st
import pandas as pd

st.title('🤖Mchine learning App')

st.info('this app is building a machine learning app')
with st.expander('Data'):
  st.write("**Raw data:**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df
  st.write('**X**')
  X = df.drop("species",axis=1) 
  X
  st.write('**y**')
  y = df.species
  y

with st.expander('Data visualisation'):
  # "bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data=df , x="bill_length_mm", y="body_mass_g", x_label="bill length",
                   y_label="body mass", color="species")
  st.line_chart(data = df,  x="bill_length_mm", y="body_mass_g", x_label="bill length",
                   y_label="body mass", color="species")
# Data preparation
with st.sidebar:
  st.header('Input features')
  # "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender', ('female','male'))
  bill_lenght_m = st.slider('Bill length (mm)', 32.1, 59.6 ,43.9)
  
