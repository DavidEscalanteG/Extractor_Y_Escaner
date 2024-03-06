1. Introducción
Este proyecto tiene como objetivo proporcionar una herramienta que permita escanear archivos PDF y extraer el texto contenido en las imágenes incrustadas en el documento. Esto facilita la extracción de información de documentos escaneados como INEs, facturas, recibos de luz, agua, entre otros, permitiendo a los usuarios llenar formularios o acceder a la información de manera más eficiente.

Propósito
El propósito principal de este proyecto es automatizar el proceso de extracción de texto de imágenes incrustadas en archivos PDF, lo que facilita la manipulación y el análisis de datos en documentos escaneados.

Componentes Principales:
Módulo de Extracción de Imágenes: Este módulo se encarga de extraer las imágenes incrustadas en el PDF utilizando la biblioteca fitz.
Módulo de Procesamiento de Imágenes: Utilizando la biblioteca easyocr, este módulo procesa las imágenes extraídas para extraer el texto contenido en ellas.
Módulo de Integración de Resultados: Este módulo integra los resultados del procesamiento de texto en un archivo de texto independiente para cada imagen.


2. Instalación y Configuración
   
Requisitos del Sistema
Python 3.12

Instalación de Python
Para instalar Python, visite el sitio oficial de Python y descargue la versión 3.12 o posterior.

Importaciones Requeridas
python
import fitz
import os
import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


3. Uso del Proyecto
Asegúrese de que el archivo PDF que desea escanear esté ubicado en la misma carpeta que el código.
Modifique el nombre del archivo PDF en la variable file_path si es necesario.
Ejecute el código para escanear el PDF y extraer el texto de las imágenes.


4. Proceso de Extracción de Texto de Imágenes

El proceso consta de los siguientes pasos:

Extracción de Imágenes del PDF: Utilizando fitz, se extraen las imágenes incrustadas en el PDF.
Procesamiento de Imágenes: Las imágenes extraídas se procesan utilizando easyocr para extraer el texto contenido en ellas.
Integración de Resultados: Los resultados del procesamiento de texto se integran y se guardan en archivos de texto independientes para cada imagen.


5. Consideraciones Adicionales
Los archivos de texto extraídos se guardarán en la carpeta 'Texto' dentro de la misma ubicación que el código.
Los nombres de los archivos PDF y los directorios de salida pueden modificarse según sea necesario.


6. Referencias y Recursos

Documentación de fitz: https://pymupdf.readthedocs.io/en/latest/module.html
Descripción: La biblioteca fitz proporciona funcionalidades para trabajar con archivos PDF en Python. Su documentación oficial ofrece información detallada sobre cómo abrir, leer, escribir y manipular archivos PDF utilizando esta biblioteca.

Documentación de easyocr: https://www.jaided.ai/easyocr/documentation/
Descripción: easyocr es una biblioteca de OCR (Reconocimiento Óptico de Caracteres) que permite extraer texto de imágenes utilizando modelos preentrenados. La documentación oficial proporciona información sobre cómo instalar, utilizar y personalizar la biblioteca para diferentes casos de uso.

Documentación de matplotlib: https://matplotlib.org/stable/index.html
Descripción: matplotlib es una biblioteca de visualización de datos en Python que se utiliza para crear gráficos, diagramas y visualizaciones. Su documentación oficial ofrece una guía completa sobre cómo crear diferentes tipos de gráficos y personalizar su apariencia.

Documentación de Pillow: https://pillow.readthedocs.io/en/stable/
Descripción: Pillow es una biblioteca de procesamiento de imágenes en Python que se utiliza para abrir, manipular y guardar imágenes en varios formatos. La documentación oficial proporciona información detallada sobre cómo utilizar las diferentes funciones y métodos de la biblioteca para realizar tareas de procesamiento de imágenes.

7. Licencia
Este proyecto se distribuye bajo la Licencia MIT.
