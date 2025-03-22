import streamlit as st

def load_css(css_file):
    """
    Carga un archivo CSS y lo aplica a la aplicación Streamlit.
    
    Args:
        css_file (str): Ruta al archivo CSS
    """
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
