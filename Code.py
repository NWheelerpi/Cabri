import numpy as numpy

parameters = np.genfromtxt('nwheelerpi/cabri/main/Parameters.txt', delimiter='|',missing_values='NA')
st.markdown(parameters)
