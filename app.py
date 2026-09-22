import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf_fun
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
    st.write("**Ubicación:** Lima - Perú")
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
    st.title("Funciones desde Librería Externa - Gestión Académica")
    st.markdown("Utiliza la clase EstudianteCurso para calcular desempeño académico")
    
    if "historico_ej3" not in st.session_state:
        st.session_state.historico_ej3 = []
    
    st.markdown("Ingresa los datos del estudiante y ejecuta los cálculos")
    
    # Inputs del estudiante
    nombre = st.text_input("Nombre del estudiante")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        actividades = st.number_input("Nota Actividades (0-20)", min_value=0.0, max_value=20.0, value=15.0)
    with col2:
        proyecto = st.number_input("Nota Proyecto (0-20)", min_value=0.0, max_value=20.0, value=16.0)
    with col3:
        examen_final = st.number_input("Nota Examen Final (0-20)", min_value=0.0, max_value=20.0, value=14.0)
    
    st.subheader("Pesos de calificación (%)")
    col1, col2, col3 = st.columns(3)
    with col1:
        peso_actividades = st.number_input("Peso Actividades", min_value=0.0, max_value=100.0, value=30.0)
    with col2:
        peso_proyecto = st.number_input("Peso Proyecto", min_value=0.0, max_value=100.0, value=40.0)
    with col3:
        peso_examen_final = st.number_input("Peso Examen Final", min_value=0.0, max_value=100.0, value=30.0)
    
    st.subheader("Asistencia")
    col1, col2 = st.columns(2)
    with col1:
        total_clases = st.number_input("Total de clases", min_value=1, value=40)
    with col2:
        clases_asistidas = st.number_input("Clases asistidas", min_value=0, value=35)
    
    if st.button("Calcular Desempeño Académico"):
        if nombre == "":
            st.error("Ingresa el nombre del estudiante")
        else:
            try:
                estudiante = lf_clase.EstudianteCurso(
                    nombre=nombre,
                    actividades=actividades,
                    proyecto=proyecto,
                    examen_final=examen_final,
                    peso_actividades=peso_actividades,
                    peso_proyecto=peso_proyecto,
                    peso_examen_final=peso_examen_final,
                    total_clases=total_clases,
                    clases_asistidas=clases_asistidas
                )
                
                resumen = estudiante.resumen()
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Nota Final", f"{resumen['nota_final']}")
                col2.metric("Asistencia", f"{resumen['asistencia_pct']}%")
                col3.metric("Estado", resumen['estado'])
                
                if resumen['estado'] == "Aprueba":
                    st.success("¡Estudiante aprobado!")
                else:
                    st.error("Estudiante no aprobado")
                
                # Agregar al histórico
                st.session_state.historico_ej3.append(resumen)
                st.success("Cálculo completado y guardado en el histórico")
                
            except ValueError as e:
                st.error(str(e))
    
    st.divider()
    st.subheader("Histórico de Estudiantes Evaluados")
    if len(st.session_state.historico_ej3) > 0:
        df_historico = pd.DataFrame(st.session_state.historico_ej3)
        st.dataframe(df_historico, use_container_width=True)
        st.write(f"Total de evaluaciones: {len(st.session_state.historico_ej3)}")
    else:
        st.info("Aún no hay estudiantes evaluados")
# EJERCICIO 4
elif pagina == "Ejercicio 4":
    st.title("CRUD")
