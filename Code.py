import numpy as np
import streamlit as st

# Extract parameter data
parameters = np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/Parameters.txt.', delimiter='|',dtype=str,skip_header=1)
actions= np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/actions.txt', delimiter='|',dtype=str)

st.markdown(type(parameters))
st.markdown(actions)
st.markdown(len(actions))
for item in range(len(parameters)):
    st.markdown(parameters[item])
    st.markdown(parameters[item][1])
    acts=''
    numbstr=parameters[item][1].split(',')
    for i in numbstr:
        try:
            inp=int(i)-1
        except:
            inp=None
        if inp==None:
            pass
        #st.markdown(inp)
        acts+=str(actions[inp][0])
    parameters[item][1]=acts
    st.markdown('Act {}'.format(acts))
    st.markdown(len(parameters[item][1]))

for item in parameters:
    st.markdown(item)
    st.markdown(item[1])
st.markdown(parameters)