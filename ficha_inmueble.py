import streamlit as st

# streamlit run D:\Dropbox\Empresa\Buydepa\COLOMBIA\DESARROLLO\streamlit\portal_inmobiliario\ficha_inmueble.py

# query params exist
try:
    options = ['cat', 'dog', 'mouse', 'bat', 'duck']

    query_params = st.experimental_get_query_params()
    query_option = query_params['option'][0] #throws an exception when visiting http://host:port

    st.text(query_option)
    st.text('id_inmueble')

except: 
    st.text('not working')