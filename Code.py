import numpy as np
#https://github.com/NWheelerpi/Cabri/blob/a046b44fc315f65b8cebdb2e7d7a713d1c2d9b28/Parameters.txt.
parameters = np.genfromtxt('https://github.com/NWheelerpi/Cabri/blob/a046b44fc315f65b8cebdb2e7d7a713d1c2d9b28/Parameters.txt.', delimiter='|',missing_values='NA')
st.markdown(parameters)
