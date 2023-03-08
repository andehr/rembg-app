import streamlit as st
from rembg import remove

from io import BytesIO
from PIL import Image


def convert_image(image):
    buf = BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


@st.cache_data
def open_image(uploaded):
    return Image.open(image_upload)


def remove_bg(image):
    return remove(image)


st.set_page_config(layout="wide", page_title="Background Remover")
with st.sidebar:
    image_upload = st.file_uploader("", type=["png", "jpg", "jpeg"])

st.title("Image Background Remover")
st.write("Upload an image in the sidebar to see the downloadable result below.")

if image_upload is None:
    image_upload = "img/squirrel.jpeg"
    loading_msg = "Processing default image..."
else:
    loading_msg = f"Processing your image `{image_upload.name}`"

with st.spinner(loading_msg):
    col_orig, col_result = st.columns(2)
    image = open_image(image_upload)
    image_fixed = remove_bg(image)
    image_downloadable = convert_image(image_fixed)

    with col_orig:
        st.subheader("Original Image")
        st.image(image_upload)

    with col_result:
        st.subheader("Result")
        st.image(image_downloadable)

    st.sidebar.download_button("Download Result", image_downloadable, file_name="result.png", mime="image/png")
