import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json

# Importaciones de páginas
from page.resume_page import resume
from page.experience_page import experience
from page.upwork_page import feedbackRating
from page.project_page import projects
from page.contact_form import contact

# Importaciones de utilidades
from utils.helpers import get_base64_image
from utils.load_css import load_css

# Page setup
st.set_page_config(
    page_title="Elvis Donayre | Portfolio",
    page_icon="📊",
    layout="wide",
)

# Cargar estilos CSS desde archivo
load_css("assets/css/style.css")

def gradient(color1, color2, color3, content1, content2):
    """
    Crea un encabezado con fondo de gradiente.
    
    Args:
        color1: Color inicial del gradiente
        color2: Color final del gradiente
        color3: Color del texto principal
        content1: Contenido principal
        content2: Contenido secundario
    """
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)
    
def aboutMe():
    """
    Sección "Acerca de mí" del portafolio.
    """
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h2 style='text-align: center; '>Hello! I'm Elvis 👋</h2>", unsafe_allow_html=True)

        st.markdown("""
        <div class="justify-text">
        I am a dedicated Data Scientist with over 4 years of professional experience in the dynamic fields of 
        machine learning and artificial intelligence. I have a proven track record in developing innovative ML models, 
        conducting in-depth data analysis, and implementing data-driven solutions that significantly impact business outcomes.
        
        I have successfully led projects across various stages of the data lifecycle, from data collection and cleaning to 
        feature engineering, modeling, and validation. I hold a Master's in Electronics (Signal Processing) and a 
        Bachelor's in Electronics and Communication 
        Engineering. I am passionate about continuous learning and advancing in the AI field.
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.markdown(
            """
            <a href="https://github.com/Elvis-Donayre" target="_blank" style="text-decoration:none;" class="social-link">
                <img src="https://img.icons8.com/?size=100&id=AZOZNnY73haj&format=png&color=000000" 
                    alt="GitHub" class="social-icon">
                <span class="social-text">GitHub</span>
            </a>
            """, 
            unsafe_allow_html=True
        )
        c2.markdown(
            """
            <a href="https://www.linkedin.com/in/elvis-donayre-data-scientist-analyst/" target="_blank" style="text-decoration:none;" class="social-link">
            <img src="https://img.icons8.com/?size=100&id=8808&format=png&color=000000"
                    alt="LinkedIn" class="social-icon">
            <span class="social-text">LinkedIn</span>
            </a>
            """, 
            unsafe_allow_html=True
        )

    # Cargar la animación desde la carpeta de assets
    path = "assets/animations/Animation - 1740107828752_2.json"
    with open(path, "r", encoding="utf-8") as file:
        url = json.load(file)
    
    with col2:
        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )

# Configuración del sidebar
# Cargar imagen para el sidebar
logo_base64 = get_base64_image("assets/images/Image.jpeg")
st.sidebar.markdown(f'<div class="logo-container"><img src="data:image/png;base64,{logo_base64}" class="logo"></div>', unsafe_allow_html=True)



with st.sidebar:
    # Option menu in sidebar
    pages = ["About me", "Resume", "Experience", "Projects", "Testimonials", "Contact"]
    nav_tab_op = option_menu(
        menu_title="Select:",
        options=pages,
        icons=['person-fill', 'file-text', 'briefcase', 'folder', 'star', 'envelope'],
        menu_icon="cast",
        default_index=0,
    )

# Main content of the app
if nav_tab_op == "About me":
    aboutMe()
elif nav_tab_op == "Resume":
    resume()
elif nav_tab_op == "Experience":
    experience()
elif nav_tab_op == "Testimonials":
    feedbackRating()
elif nav_tab_op == "Projects":
    projects()
elif nav_tab_op == "Contact":
    contact()