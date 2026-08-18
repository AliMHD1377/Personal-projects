import streamlit as st
import pandas as pd

st.write('Hello!')
st.write("Ali")

"ali mohammadi"

"""
alo

hi
"""

df = pd.DataFrame(
    {
        "first colum":[1, 2, 3, 4],
        "second colum":[20, 22, 45, 89]
    }
)
df

st.slider('select a value', 10, 50, 20)

st.selectbox('yekibardar', ('book', 'phone', 'laptop'))
st.multiselect("yekibardar", ('book', 'phone', 'laptop'))
if st.checkbox("salam"):
    "aleike salam"

col1, col2, col3 = st.columns(3)
col1.write("salam")
col2.checkbox("col2")
col3.multiselect("col3", ('book', 'phone', 'laptop'))

x = st.slider('x')  # this is a widget
st.write(x, 'squared is', x * x)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')