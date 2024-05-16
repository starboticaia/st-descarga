import streamlit as st

nombre = st.text_input("Introduzca su nombre",value="nombre")
fecha_nac = st.date_input("Fecha de nacimiento")

texto = f'''Nombre: {nombre}
Fecha de nacimiento: {fecha_nac}
'''

# Different ways to use the API

if st.download_button('Descargar', texto):
  st.write("Descarga realizada")
