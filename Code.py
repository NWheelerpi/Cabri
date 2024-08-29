import numpy as np
import streamlit as st

# Extract parameter data
parameters = np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/Parameters.txt.', delimiter='|',dtype=str)

actions=[]
for item in parameters:
    if ' \ ' in item[2]:
        sub_actions=item[2].split(' \ ')
    else:
        sub_actions=item[2]
    actions.append(sub_actions)

for i in parameters
    st.markdown(i)
st.markdown(actions)