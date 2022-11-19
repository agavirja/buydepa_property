import streamlit as st

# streamlit run D:\Dropbox\Empresa\Buydepa\COLOMBIA\DESARROLLO\streamlit\portal_inmobiliario\ficha_inmueble.py

# https://agavirja-buydepa-property-ficha-inmueble-66hgl1.streamlit.app/
# https://agavirja-buydepa-property-ficha-inmueble-66hgl1.streamlit.app/?option=15435

# query params exist
try:
    query_params = st.experimental_get_query_params()
    query_option = query_params['option'][0] #throws an exception when visiting http://host:port
    st.text(query_option)
    st.text('id_inmueble')

except: 
    st.text('not working')