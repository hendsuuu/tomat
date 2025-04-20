TomatVision App ver 1.0 
********************************
cara launch:
1. Import Database dbtomat.sql
   - ke file db.py sesuaikan username dan password database kamu
Buka terminal :
2. install bcrypt: pip install bcrypt streamlit
3. install mysql connector : pip install mysql-connector-python
4. install tensorFlow : pip install streamlit tensorflow pillow
5. install opencv : pip install streamlit opencv-python tensorflow pillow
6. run xampp/wampp/lampp/db kalian
7. run aplikasi : streamlit run main.py
===========================================================================================
how to use
1. login menggunakan username dan password, jika belum punya akun signup terlebih dahulu.
2. isi captcha.
3. setelah di halaman home, jika mau scan/upload gambar tomat langsung ke navigasi pilih "Camera scan".
4. centang nyalakan kamera untuk scan / klik upload gambar untuk metode upload.
5. setelah itu akan keluar hasilnya.
6. untuk melihat riwayat scan dan upload bisa ke navigasi pilih "Gallery & Photo Details".
7. klik detail untuk melihat detail prediction.
8. klik hapus untuk menghapus gambar tersebut.