import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def resume():
    # Actualizar ruta del archivo PDF
    pdf_path = "assets/documents/archana.pdf"
    
    with open(pdf_path, "rb") as pdf_file:
        document = pdf_file.read()

    st.markdown("""
            <style>
            .stDownloadButton button {
                background-color: #1E9E35 !important;
                color: white !important;
            }
            </style>
            """, unsafe_allow_html=True)

    st.download_button(
                label="Download Resume",
                key="download_button",
                file_name="archana.pdf",
                data=document,
                help="Click to download.",
            )
            
    with st.container():
        st.markdown(
            """
            <style>
            .stContainer > div {
                width: 55%;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Actualizar ruta del archivo PDF
        pdf_viewer(pdf_path)
