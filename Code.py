import numpy as np

parameters = np.genfromtxt('repo/Parameters.txt', delimiter='|',missing_values='NA')
st.markdown(parameters)
