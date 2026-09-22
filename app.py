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
    
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []
    
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor")

    if st.button("Agregar movimiento"):
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
            st.session_state.movimientos.append(nuevo)
            st.success("Movimiento agregado")
    
    if len(st.session_state.movimientos) > 0:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df)
        
        ingresos = df[df["tipo"] == "Ingreso"]["valor"].sum()
        gastos = df[df["tipo"] == "Gasto"]["valor"].sum()
        saldo = ingresos - gastos
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Ingresos", f"S/. {ingresos:.1f}")
        col2.metric("Gastos", f"S/. {gastos:.1f}")
        col3.metric("Saldo", f"S/. {saldo:.1f}")
        
# EJERCICIO 2
elif pagina == "Ejercicio 2":
    st.title("Registro NumPy")

    if "registros" not in st.session_state:
        st.session_state.registros = []
    
    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Electrónica", "Ropa", "Alimentos"])
    precio = st.number_input("Precio", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=0)
    
    if st.button("Agregar registro"):
        if nombre == "":
            st.error("Ingresa el nombre del producto")
        elif precio <= 0:
            st.error("El precio debe ser mayor que cero")
        elif cantidad <= 0:
            st.error("La cantidad debe ser mayor que cero")
        else:
            total = precio * cantidad
            
            nuevo = {
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
                "cantidad": cantidad,
                "total": total
            }
            st.session_state.registros.append(nuevo)
            st.success("Registro agregado")
    
    # MOSTRAR TABLA
    if len(st.session_state.registros) > 0:
        df = pd.DataFrame(st.session_state.registros)
        st.dataframe(df)
    else:
        st.info("Aún no hay registros")

# EJERCICIO 3
elif pagina == "Ejercicio 3":
    st.title("Funciones Externas")

# EJERCICIO 4
elif pagina == "Ejercicio 4":
    st.title("CRUD")
