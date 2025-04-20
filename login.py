import streamlit as st
from auth import verify_user
from captcha import generate_captcha, check_captcha

def login_page():
    st.title("Halaman Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    generated_captcha = st.session_state.get("generated_captcha", generate_captcha())
    st.session_state["generated_captcha"] = generated_captcha

    st.markdown(f"<b>CAPTCHA:</b> {generated_captcha}</p>", unsafe_allow_html=True)
    input_captcha = st.text_input("Masukkan CAPTCHA")

    if st.button("Login"):
        if not check_captcha(input_captcha, generated_captcha):
            st.error("CAPTCHA salah")
        elif verify_user(username, password):
            st.success("Login berhasil!")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.experimental_rerun()
        else:
            st.error("Username atau password salah")
