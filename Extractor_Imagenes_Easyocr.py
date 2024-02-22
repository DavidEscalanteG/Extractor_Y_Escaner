import fitz
import os
import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Crear las carpetas si no existen
output_folder = 'Imagenes'
text_output_folder = 'Texto'
os.makedirs(output_folder, exist_ok=True)
os.makedirs(text_output_folder, exist_ok=True)

file_path = 'Pdf_1.pdf'

try:
    # Abrir el archivo PDF
    pdf_file = fitz.open(file_path)

    images_list = []

    # Guardar las imágenes en archivos separados
    for page_num in range(len(pdf_file)):
        page_content = pdf_file[page_num]
        images = page_content.get_images()
        for i, image in enumerate(images, start=1):
            xref = image[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"{page_num + 1}_{i}.{image_ext}"

            # Guardar la imagen
            image_path = os.path.join(output_folder, image_name)
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            images_list.append((image_path, page_num))

    # Configurar el lector de easyocr para español
    reader = easyocr.Reader(['es'])

    # Procesar el texto de las imágenes guardadas
    for image_path, page_num in images_list:
        # Procesar el texto de la imagen
        result = reader.readtext(image_path)

        # Abrir la imagen
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Visualizar la imagen y las cajas delimitadoras
        fig, ax = plt.subplots(1)
        ax.imshow(img)

        for detection in result:
            bbox = detection[0]
            text = detection[1]

            # Convertir las coordenadas de la caja delimitadora al formato de matplotlib
            left = bbox[0][0] / img_width
            top = bbox[0][1] / img_height
            width = (bbox[1][0] - bbox[0][0]) / img_width
            height = (bbox[1][1] - bbox[0][1]) / img_height

            # Agregar un rectángulo para visualizar la caja delimitadora
            rect = patches.Rectangle((left, top), width, height,
                                     linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            # Agregar el texto detectado
            ax.text(left, top, text, color='r', fontsize=8, verticalalignment='top')

        # Configurar los ejes de la imagen
        ax.axis('off')

        # Mostrar la imagen visualizada en una ventana emergente
        plt.show()

        # Guardar la imagen visualizada
        visualized_image_path = f"visualized_{os.path.basename(image_path)}"
        plt.savefig(visualized_image_path)
        plt.close()

        # Guardar el texto en un archivo txt
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        text_file_name = f"{image_name}.txt"
        text_file_path = os.path.join(text_output_folder, text_file_name)
        with open(text_file_path, "w") as text_file:
            for detection in result:
                text_file.write(detection[1] + '\n')

    print("Imágenes y texto extraídos correctamente")
except Exception as e:
    print(f"Error: {e}")
