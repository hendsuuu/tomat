import streamlit as st
from auth import add_user

def signup_page():
    st.title("Halaman Signup")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Konfirmasi Password", type="password")
    
    if st.button("Signup"):
        if password != confirm_password:
            st.error("Password dan Konfirmasi Password tidak cocok")
        elif add_user(username, password):
            st.success("Signup berhasil! Silakan login.")
        else:
            st.error("Username sudah digunakan")
