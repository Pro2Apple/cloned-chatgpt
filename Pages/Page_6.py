import streamlit as st

st.write(st.session_state)

if "a" not in st.session_state:
    st.session_state.a = 0

button = st.button("加1")

if button:
    st.session_state.a += 1
st.write(st.session_state.a)
st.write(st.session_state)