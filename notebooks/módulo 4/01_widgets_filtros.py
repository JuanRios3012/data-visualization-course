# Ejemplo 1: Widgets e interactividad con Streamlit
# Demuestra el uso de selectbox y slider para filtrar datos

import streamlit as st
import pandas as pd
import seaborn as sns

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset('penguins')

st.title('Ejemplo de filtros con Streamlit')

# Crear un selectbox para escoger la especie
especie = st.selectbox('Selecciona la especie', df['species'].unique())

# Crear un slider para elegir un rango de masa corporal
masa_min, masa_max = st.slider('Rango de masa corporal (g)',
                               min_value=float(df['body_mass_g'].min()),
                               max_value=float(df['body_mass_g'].max()),
                               value=(float(df['body_mass_g'].min()), float(df['body_mass_g'].max())))

# Filtrar datos según los valores seleccionados
df_filtrado = df[(df['species'] == especie) & (df['body_mass_g'] >= masa_min) & (df['body_mass_g'] <= masa_max)]

# Mostrar una tabla con los datos filtrados
# Convertir columnas de string a object para compatibilidad con Streamlit 1.19.0
df_display = df_filtrado.copy()
for col in df_display.select_dtypes(include=['string']).columns:
    df_display[col] = df_display[col].astype('object')
st.dataframe(df_display)
