import numpy as np

parameters = np.genfromtxt('Parameters.txt', delimiter='|',missing_values='NA')
st.markdown(parameters)
