import numpy as np
import streamlit as st

# Extract parameter data
parameters = np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/Parameters.txt.', delimiter='|',dtype=str,skip_header=1)
actions= np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/actions.txt', delimiter='|',dtype=str)
parameters=parameters.tolist()

#st.markdown(actions)

# Exchange string of numbers for actions from actions list
for item in range(len(parameters)):
    acts=''
    numbstr=parameters[item][1].split(',')
    for i in numbstr:
        try:
            inp=int(i)-1
        except:
            inp=None
        if inp==None:
            pass
        acts+=str(actions[inp][0])
    parameters[item][1]=acts

for item in parameters:
    st.markdown(item)
#st.markdown(parameters)

