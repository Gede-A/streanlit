import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.utils import fetch_data, process_data

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interactive Data Dashboard", layout="wide")

st.title('Interactive Data Dashboard')
st.header('Explore data interactively using Streamlit')

data = fetch_data()
processed_data = process_data(data)

range_filter = st.slider('Select Range:', 0, 100, (10, 50))
category_filter = st.selectbox('Select Category:', options=processed_data['category'].unique())

filtered_data = processed_data[
    (processed_data['value'] >= range_filter[0]) & 
    (processed_data['value'] <= range_filter[1]) &
    (processed_data['category'] == category_filter)
]

st.write(filtered_data)

st.line_chart(filtered_data['value'])
