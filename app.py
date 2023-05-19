import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers

headers = _get_websocket_headers()

st.write("Hello")

st.write(st.experimental_user)

st.write(headers)