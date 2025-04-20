import streamlit as st
from login import login_page
from signup import signup_page
from index import camera_scan_page, gallery_and_details_page, homepage
from db import check_db_connection

def set_custom_css():
    st.markdown(
        """
        <style>
            .main .sidebar .sidebar-content {
                background-color: #d3d3d3 !important;  
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    set_custom_css()

    st.sidebar.title("Navigasi")

    # Periksa koneksi database dan tampilkan status
    if check_db_connection():
        st.sidebar.success("Koneksi ke database berhasil")
    else:
        st.sidebar.error("Gagal terhubung ke database")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Jika pengguna sudah login, sembunyikan select box
    if not st.session_state["logged_in"]:
        page = st.sidebar.selectbox("Pilih Halaman", ["Login", "Signup"])
        if page == "Login":
            login_page()
        elif page == "Signup":
            signup_page()
    else:
        st.sidebar.write(f"Selamat datang, {st.session_state['username']}!")
        page = st.sidebar.selectbox("Pilih halaman", ["Home", "Camera Scan", "Gallery & Photo Details"])
        if page == "Home":
            homepage()
        elif page == "Camera Scan":
            camera_scan_page()
        elif page == "Gallery & Photo Details":
            gallery_and_details_page() 
            
        if st.sidebar.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["generated_captcha"] = None  # Reset CAPTCHA setelah logout
            st.experimental_rerun()  # Rerun aplikasi setelah logout    
            
if __name__ == "__main__":
    main()
