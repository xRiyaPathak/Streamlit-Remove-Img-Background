# This is the code to remove background from an image.

import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.markdown("<h1 style='text-align: center; color: black;'> Remove background from your image  </h1>", unsafe_allow_html=True)


st.write(":star: This is an app where you can upload an image and the background will be removed!!!!!! :star:")
st.write(":camera_with_flash: You also have the option to download your image. :camera_with_flash:")

st.sidebar.write("## Upload the Image :bangbang:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the final image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def final_image(upload):
    image = Image.open(upload)
    col1.write("#### Original Image :arrow_double_down:")
    col1.image(image)

    final = remove(image)
    col2.write("#### Image without Background :arrow_double_down:")
    col2.image(final)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download :inbox_tray:", convert_image(final), "final.png", "image/png", use_container_width=True)


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload :outbox_tray:", type=["png", "jpg", "jpeg"])

st.sidebar.write("## Download the Image :bangbang:")

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        final_image(upload=my_upload)
else:
    final_image("./animal.jpg")