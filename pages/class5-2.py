import streamlit as st
import os

st.title("圖片元素")
image_folder = "image"
image_files = os.listdir(image_folder)

image_size = st.number_input("請輸入圖片的大小", min_value=1, value=100, step=10)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", use_container_width=True)
select_image = st.selectbox("請選擇圖片", image_files)
st.image(f"{image_folder}/{select_image}", width=image_size)
