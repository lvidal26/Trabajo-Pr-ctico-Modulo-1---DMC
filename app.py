
import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import pandas as pd

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
    
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor")

    # BOTÓN
    if st.button("Agregar movimiento"):
        # VALIDACIÓN SIMPLE
        if concepto == "":
            st.error("Debes ingresar un concepto")
        elif valor <= 0:
            st.error("El valor debe ser mayor que cero")
        else:
            nuevo = {
                "concepto": concepto,
                "tipo": tipo,
                "valor": valor
            }
            movimientos.append(nuevo)
            st.success("Movimiento agregado")
            st.rerun()
    
    # RESULTADOS
    if len(movimientos) > 0:
        df = pd.DataFrame(movimientos)
        st.dataframe(df)
        
        ingresos = df[df["tipo"] == "Ingreso"]["valor"].sum()
        gastos = df[df["tipo"] == "Gasto"]["valor"].sum()
        saldo = ingresos - gastos
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Ingresos", f"S/. {ingresos:.2f}")
        col2.metric("Gastos", f"S/. {gastos:.2f}")
        col3.metric("Saldo", f"S/. {saldo:.2f}")

# EJERCICIO 2
elif pagina == "Ejercicio 2":
    st.title("Registro NumPy")

# EJERCICIO 3
elif pagina == "Ejercicio 3":
    st.title("Funciones Externas")

# EJERCICIO 4
elif pagina == "Ejercicio 4":
    st.title("CRUD")
