
import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf


# CREAR LA NAVEGACIÓN
pagina = st.sidebar.selectbox(
    "Menú",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# HOME
if pagina == "Home":
    st.title("Home")
    st.image("logo dmc.png", width = 300)
    st.sidebar.image("logo dmc.png")
    st.write("Bienvenido al proyecto Módulo 1 – Python Fundamentals")
    st.write("**Nombre:** Luis Vidal")
    st.write("**Edad:** 18 años")
    st.write("**Ubicación:** Lima")
    st.write("**Año:** 2026")
    
    st.divider()
    
    st.write("**Descripción:** Proyecto de Streamlit con 4 ejercicios de Python")
    
    st.divider()
    
    st.write("**Tecnologías:** Python • Streamlit • Pandas • NumPy")

# EJERCICIO 1
elif pagina == "Ejercicio 1":
    st.title("Flujo de Caja")
    st.write("Tus funciones del Ejercicio 1 aquí")

# EJERCICIO 2
elif pagina == "Ejercicio 2":
    st.title("Registro NumPy")
    st.write("Tus funciones del Ejercicio 2 aquí")

# EJERCICIO 3
elif pagina == "Ejercicio 3":
    st.title("Funciones Externas")
    st.write("Tus funciones del Ejercicio 3 aquí")

# EJERCICIO 4
elif pagina == "Ejercicio 4":
    st.title("CRUD")
    st.write("Tus funciones del Ejercicio 4 aquí")
