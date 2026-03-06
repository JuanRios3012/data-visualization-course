# Ejemplo 2: Layout y contenedores
# Demuestra el uso de sidebar y columnas para organizar la interfaz

import streamlit as st
import pandas as pd
import numpy as np

st.title('Dashboard con barra lateral y columnas')

# Widgets en la barra lateral
with st.sidebar:
    st.header('Opciones de filtrado')
    rango = st.slider('Selecciona un rango', 0, 100, (25, 75))
    opcion = st.radio('Mostrar gráficos', ['Histograma', 'Dispersión'])

# Generar datos aleatorios
np.random.seed(0)
datos = np.random.randn(500)
datos_filtrados = datos[(datos >= (rango[0] - 50) / 10) & (datos <= (rango[1] - 50) / 10)]

# Layout en columnas
a, b = st.columns(2)

# Mostrar resultados en columnas
with a:
    st.subheader('Datos filtrados')
    df_display = pd.DataFrame({'Valores': datos_filtrados})
    st.write(df_display)

with b:
    if opcion == 'Histograma':
        st.subheader('Histograma')
        st.bar_chart(pd.DataFrame({'Valores': datos_filtrados}))
    else:
        st.subheader('Diagrama de dispersión')
        st.scatter_chart(pd.DataFrame({'x': np.arange(len(datos_filtrados)), 'y': datos_filtrados}))
