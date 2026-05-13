import streamlit as st
from PIL import Image
import pytesseract
import tempfile

st.set_page_config(page_title="OCR Document Reader")

st.title("📄 OCR Document Reader")
st.write("Upload a document image and extract text from it.")

uploaded_file = st.file_uploader(
    "Upload Document Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Extract Text"):

        extracted_text = pytesseract.image_to_string(image)

        st.subheader("Extracted Text")

        st.text_area(
            "Output",
            extracted_text,
            height=300
        )

        # Save text file
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".txt"
        )

        with open(temp_file.name, "w", encoding="utf-8") as f:
            f.write(extracted_text)

        with open(temp_file.name, "rb") as f:
            st.download_button(
                label="📥 Download Text File",
                data=f,
                file_name="extracted_text.txt",
                mime="text/plain"
            )
