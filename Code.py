import numpy as np
import streamlit as st

# Extract parameter data
parameters = np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/Parameters.txt.', delimiter='|',dtype=str)
actions= np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/actions.txt', delimiter=1,dtype=str)
#
#actions=[]
#for item in parameters:
#    if '\\' in item[2]:
#        sub_actions=item[2].split('\\')
#        for i in sub_actions:
#            if i not in actions:
#                actions.append(i)
#    else:
#        if item[2] not in actions:
#            actions.append(str(item[2]))

for i in parameters:
    st.markdown(i)
st.markdown(actions)