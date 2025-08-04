""" Ejercicios ETL Parte II
Continuarás trabajando con los datos limpios y transformados de los ejercicios de ETL I para crear una base de datos y cargar los datos en ella.

Los pasos del ejercicio son:

Creación de la Base de Datos:
1.Utilizar MySQL para crear una base de datos vacía. 
2.Definir la estructura de la base de datos: esquemas de tablas, relaciones entre ellas, etc.
3.Carga de Datos en la Base de Datos:
4.Utilizar Python + SQL para insertar los datos transformados el día anterior.

NOTA Este ejercicio debe realizarse en un archivo .py """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, kstest
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("df_pair.csv")


query = """
INSERT INTO clientes (
    id_cliente, id_producto, fecha_venta, cantidad, total,
    first_name, last_name, email, gender, city, country,
    address, nombre_producto, categoria, precio, origen,
    descripcion
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s
);
"""

valores = (
    723, 'A1', '2023-11-22', 2, 17.98,
    'Sephira', 'Bleackley', 'sbleackleyk2@liveinternet.ru', 'NaN', 'Girona', 'NaN',
    '4 Birchwood Road', 'Pizza Margherita', 'Platos Preparados', 8.99, 'Italia',
    'Clásica pizza italiana con tomate'
)

cursor.execute(query, valores)
