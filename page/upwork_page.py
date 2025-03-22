import streamlit as st
from streamlit_lottie import st_lottie
import json

def feedbackRating():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="centered-header">
                <h2>Testimonials </h2>
            </div>
        """, unsafe_allow_html=True)
    
    # Actualizar ruta de la animación
    path = "assets/animations/Animation_rating.json"
    with open(path, "r") as file:
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
    
    with st.container():
        st.markdown("### Ranked top 10% of all Upwork talent")
        st.write("#### Achieved a Top Rated badge with a 100% Job Success Rate on Upwork.")
        st.write("To verify the following information related to Upwork, please use this [link](https://www.upwork.com/freelancers/~010f3758a004ea64dd?viewMod).")
        
        # Actualizar ruta de la imagen
        st.image('assets/images/up_10R.png', width=700)

        with st.container():
            st.write("### Testimonials From Clients")
            
            # Actualizar rutas de las imágenes
            image_paths = [
                "assets/images/up1.png", 
                "assets/images/up2.png", 
                "assets/images/up3.png", 
                "assets/images/up4.png", 
                "assets/images/up.png"
            ]
            
            for i in range(5):
                if i % 2 == 0:
                    col1, col2, col3 = st.columns([1, 1, 4])
                    col3.image(image_paths[i], width=700)
                else:
                    col1, col2, col3 = st.columns([4, 1, 1])
                    col1.image(image_paths[i], width=700)
