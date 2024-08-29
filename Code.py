import numpy as np

parameters = np.genfromtxt('NWheelerpi/Cabri/main/Parameters.txt', delimiter='|',missing_values='NA')
st.markdown(parameters)
