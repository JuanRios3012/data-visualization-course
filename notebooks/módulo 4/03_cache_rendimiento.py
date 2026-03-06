# Ejemplo 3: Caché y rendimiento
# Demuestra el uso de @st.cache_data para optimizar la carga de datos

import streamlit as st
import pandas as pd
import time

@st.cache_data
def cargar_datos(path):
    # Simula una operación costosa
    time.sleep(3)
    return pd.read_csv(path)

st.title('Ejemplo de caché en Streamlit')

st.write('Cargando datos...')
df = cargar_datos('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
st.success('Datos cargados')
# Convertir columnas de string a object para compatibilidad
df_display = df.head().copy()
for col in df_display.select_dtypes(include=['string', 'object']).columns:
    if df_display[col].dtype == 'string':
        df_display[col] = df_display[col].astype('object')
st.write(df_display)

st.info('💡 La primera vez tardará 3 segundos. Las siguientes veces será instantáneo gracias al caché.')
