# Portfolio - Elvis Donayre

## Descripción
Este es mi portafolio personal como Data Scientist, desarrollado con Streamlit. Muestra mi experiencia profesional, habilidades, proyectos y permite a los visitantes contactarme.

## Estructura del Proyecto
```
Portfolio-main/
│
├── app.py                          # Archivo principal 
│
├── pages/                          # Páginas individuales
│   ├── __init__.py                 # Hace que pages sea un módulo Python
│   ├── resume_page.py              # Página de resumen/CV
│   ├── experience_page.py          # Página de experiencia
│   ├── upwork_page.py              # Página de testimonios de Upwork
│   ├── project_page.py             # Página de proyectos
│   └── contact_form.py             # Formulario de contacto
│
├── utils/                          # Funciones de utilidad
│   ├── __init__.py                 # Hace que utils sea un módulo Python
│   ├── load_css.py                 # Función para cargar CSS
│   └── helpers.py                  # Funciones auxiliares
│
├── assets/                         # Recursos estáticos
│   ├── css/                        # Estilos CSS
│   ├── images/                     # Imágenes
│   ├── animations/                 # Animaciones Lottie
│   └── documents/                  # Documentos como PDFs
│
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Documentación del proyecto
```

## Características
- Diseño responsive
- Navegación intuitiva con menú lateral
- Animaciones interactivas con Lottie
- Visualización de CV con opción de descarga
- Formulario de contacto
- Visualización detallada de proyectos
- Testimonios de clientes

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/Elvis-Donayre/portfolio.git
cd portfolio
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run app.py
```

## Tecnologías Utilizadas
- Python
- Streamlit
- HTML/CSS
- Streamlit Lottie para animaciones
- Streamlit PDF Viewer para visualización de documentos

## Contacto
- GitHub: [Elvis-Donayre](https://github.com/Elvis-Donayre)
- LinkedIn: [Elvis Donayre](https://www.linkedin.com/in/elvis-donayre-data-scientist-analyst/)

## Licencia
Este proyecto está bajo la licencia MIT.
