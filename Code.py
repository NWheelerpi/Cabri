import numpy as np
import streamlit as st

# Extract parameter data
parameters = np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/Parameters.txt.', delimiter='|',dtype=str)

actions=[]
for item in parameters:
    if '\' in item 

st.markdown(parameters[0])