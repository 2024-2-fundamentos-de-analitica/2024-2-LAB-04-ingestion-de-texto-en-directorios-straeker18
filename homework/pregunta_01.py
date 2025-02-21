# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import os
import zipfile

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    directorio_entrada = 'files/input'
    directorio_salida = 'files/output'
    conjuntos = ['train', 'test']
    etiquetas = ['positive', 'negative', 'neutral']
    
    os.makedirs(directorio_salida, exist_ok=True)
    
    for conjunto in conjuntos:
        datos = []
        ruta_conjunto = os.path.join(directorio_entrada, conjunto)
        
        for etiqueta in etiquetas:
            ruta_etiqueta = os.path.join(ruta_conjunto, etiqueta)
            
            for archivo in os.listdir(ruta_etiqueta):
                ruta_archivo = os.path.join(ruta_etiqueta, archivo)
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_texto:
                    contenido = archivo_texto.read().strip()
                datos.append({'phrase': contenido, 'target': etiqueta})
        
        archivo_salida = os.path.join(directorio_salida, f"{conjunto}_dataset.csv")
        pd.DataFrame(datos).to_csv(archivo_salida, index=False)

pregunta_01()