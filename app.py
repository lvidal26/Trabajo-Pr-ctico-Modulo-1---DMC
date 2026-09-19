
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
    st.subheader("Bienvenido al proyecto Módulo 1 – Python Fundamentals")
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
    
    movimientos = []
    
    if st.button("Agregar movimiento"):
        nuevo = {
            "concepto": concepto,
            "tipo": tipo,
            "valor": valor
        }
        movimientos.append(nuevo)

# EJERCICIO 2
elif pagina == "Ejercicio 2":
    st.title("Registro NumPy")

# EJERCICIO 3
elif pagina == "Ejercicio 3":
    st.title("Funciones Externas")

# EJERCICIO 4
elif pagina == "Ejercicio 4":
    st.title("CRUD")
