import streamlit as st
import pandas as pd
import numpy as np

st.title('**st.line_chart**')
st.write('*Allows writing text and arguments to the Streamlit app!*')


st.header('Line chart')

# A dataFrame of randomly generated numbers that contains 3 columns
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

# Displays a line chart 
st.line_chart(chart_data)