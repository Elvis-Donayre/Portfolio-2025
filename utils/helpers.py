import requests
import base64

def load_lottieurl(url: str):
    """
    Carga un archivo JSON de Lottie desde una URL.
    
    Args:
        url (str): URL del archivo JSON Lottie
        
    Returns:
        dict: Objeto JSON de Lottie o None si hay error
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_base64_image(image_path):
    """
    Convierte una imagen en una cadena base64.
    
    Args:
        image_path (str): Ruta al archivo de imagen
        
    Returns:
        str: Cadena base64 de la imagen
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
