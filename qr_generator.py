import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="🔲", layout="centered")

st.title("🔲 QR Code Generator")
st.write("Enter text or a URL to generate your QR Code instantly.")

# User input
qr_text = st.text_input("Enter Text or URL", "")

if st.button("Generate QR Code"):
    if qr_text.strip() != "":
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(qr_text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Display image
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.image(buf.getvalue(), caption="Your QR Code", use_column_width=True)

        # Download button
        st.download_button(
            label="Download QR Code",
            data=buf.getvalue(),
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.error("Please enter some text or URL first.")
