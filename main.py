import qrcode
import os
import re

def limpiar_nombre(url):
    nombre = re.sub(r'^https?:\/\/(www\.)?', '', url)
    nombre_seguro = re.sub(r'[\/\\?%*:|"<>]', '_', nombre)
    return nombre_seguro.strip('_') + ".png"

def generar_qr(url):
    carpeta_destino = "qr-code's"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"Carpeta '{carpeta_destino}' creada.")

    nombre_archivo = limpiar_nombre(url)
    
    ruta_completa = os.path.join(carpeta_destino, nombre_archivo)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar en la ruta específica
    img.save(ruta_completa)
    print(f"¡Listo! QR de la página guardado en: {ruta_completa}")

if __name__ == "__main__":
    enlace = input("Ingresa la URL que deseas convertir: ")
    if enlace.strip():
        generar_qr(enlace)
    else:
        print("No ingresaste ninguna URL.")