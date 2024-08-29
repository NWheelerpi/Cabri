import numpy as np
import streamlit as st

#parameters = np.genfromtxt('https://github.com/NWheelerpi/Cabri/blob/a046b44fc315f65b8cebdb2e7d7a713d1c2d9b28/Parameters.txt.', delimiter='|',dtype=None)
#parameters = np.genfromtxt('https://github.com/NWheelerpi/Cabri/blob/20f70220d87bd70c4e4bc25df4ae63adb4620f9c/Test.txt', delimiter='|')
parameters = np.genfromtxt('https://raw.githubusercontent.com/NWheelerpi/Cabri/main/Parameters.txt.', delimiter='|',dtype=str)
#parameters = open('https://github.com/NWheelerpi/Cabri/blob/a046b44fc315f65b8cebdb2e7d7a713d1c2d9b28/Parameters.txt.','r')
for i in parameters:
    st.markdown(i)