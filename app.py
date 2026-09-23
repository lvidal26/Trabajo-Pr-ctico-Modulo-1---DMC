import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lf_clase
import pandas as pd


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
    st.title("CRUD - Gestión de Empleados")
    st.markdown("Crea, lee, actualiza o elimina registros de empleados usando la clase Empleado.")
    
    if "empleados_ej4" not in st.session_state:
        st.session_state.empleados_ej4 = []
        
    tab1, tab2, tab3, tab4 = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])
    

    with tab1:
        st.subheader("Crear Nuevo Empleado")
        st.markdown("Completa el formulario para agregar un nuevo empleado")
        
        nombre = st.text_input("Nombre del empleado", key="crear_nombre")
        col1, col2 = st.columns(2)
        with col1:
            salario_base = st.number_input("Salario base (S/.)", min_value=0.0, value=2000.0, key="crear_salario")
        with col2:
            porcentaje_bono = st.number_input("Porcentaje bono (%)", min_value=0.0, max_value=100.0, value=10.0, key="crear_bono")
        
        col1, col2 = st.columns(2)
        with col1:
            porcentaje_descuento = st.number_input("Porcentaje descuento (%)", min_value=0.0, max_value=100.0, value=5.0, key="crear_descuento")
        
        if st.button("Crear Empleado", key="btn_crear"):
            if nombre == "":
                st.error("Ingresa el nombre del empleado")
            else:
                try:
                    nuevo_empleado = lf_clase.Empleado(
                        nombre=nombre,
                        salario_base=salario_base,
                        porcentaje_bono=porcentaje_bono,
                        porcentaje_descuento=porcentaje_descuento
                    )
                    st.session_state.empleados_ej4.append(nuevo_empleado)
                    st.success(f"Empleado '{nombre}' creado correctamente")
                except ValueError as e:
                    st.error(str(e))
    
  
    with tab2:
        st.subheader("Visualizar Todos los Empleados")
        
        if len(st.session_state.empleados_ej4) > 0:
            st.markdown(f"**Total de empleados:** {len(st.session_state.empleados_ej4)}")
            
            datos = [emp.resumen() for emp in st.session_state.empleados_ej4]
            df = pd.DataFrame(datos)
            st.dataframe(df, use_container_width=True)
            
            # Estadísticas
            st.divider()
            st.subheader("Estadísticas")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total de empleados", len(st.session_state.empleados_ej4))
            col2.metric("Salario promedio", f"S/. {df['salario_base'].mean():.2f}")
            col3.metric("Total bonos", f"S/. {df['bono'].sum():.2f}")
            col4.metric("Nómina total", f"S/. {df['salario_neto'].sum():.2f}")
        else:
            st.info("No hay empleados registrados aún")
    
   
    with tab3:
        st.subheader("Actualizar Empleado")
        
        if len(st.session_state.empleados_ej4) > 0:
            nombres = [emp.nombre for emp in st.session_state.empleados_ej4]
            indice = st.selectbox("Selecciona el empleado a actualizar:", range(len(nombres)), format_func=lambda x: nombres[x], key="select_actualizar")
            
            empleado_actual = st.session_state.empleados_ej4[indice]
            resumen_actual = empleado_actual.resumen()
            
            st.markdown("**Datos actuales:**")
            col1, col2, col3 = st.columns(3)
            col1.metric("Salario Base", f"S/. {resumen_actual['salario_base']}")
            col2.metric("Bono", f"S/. {resumen_actual['bono']}")
            col3.metric("Salario Neto", f"S/. {resumen_actual['salario_neto']}")
            
            st.divider()
            st.markdown("**Ingresa los nuevos valores:**")
            
            nombre_nuevo = st.text_input("Nombre", value=empleado_actual.nombre, key="act_nombre")
            col1, col2 = st.columns(2)
            with col1:
                salario_nuevo = st.number_input("Salario base (S/.)", min_value=0.0, value=float(empleado_actual.salario_base), key="act_salario")
            with col2:
                bono_nuevo = st.number_input("Porcentaje bono (%)", min_value=0.0, max_value=100.0, value=float(empleado_actual.porcentaje_bono), key="act_bono")
            
            col1, col2 = st.columns(2)
            with col1:
                descuento_nuevo = st.number_input("Porcentaje descuento (%)", min_value=0.0, max_value=100.0, value=float(empleado_actual.porcentaje_descuento), key="act_descuento")
            
            if st.button("Guardar Cambios", key="btn_actualizar"):
                try:
                    empleado_actualizado = lf_clase.Empleado(
                        nombre=nombre_nuevo,
                        salario_base=salario_nuevo,
                        porcentaje_bono=bono_nuevo,
                        porcentaje_descuento=descuento_nuevo
                    )
                    st.session_state.empleados_ej4[indice] = empleado_actualizado
                    st.success("Empleado actualizado correctamente")
                except ValueError as e:
                    st.error(str(e))
        else:
            st.info("No hay empleados para actualizar")
    
    with tab4:
        st.subheader("Eliminar Empleado")
        
        if len(st.session_state.empleados_ej4) > 0:
            nombres = [emp.nombre for emp in st.session_state.empleados_ej4]
            indice = st.selectbox("Selecciona el empleado a eliminar:", range(len(nombres)), format_func=lambda x: nombres[x], key="select_eliminar")
            
            # Mostrar confirmación solo después de seleccionar
            empleado_seleccionado = st.session_state.empleados_ej4[indice]
            resumen = empleado_seleccionado.resumen()
            
            st.divider()
            st.warning(f"¿Estás seguro de que deseas eliminar a **{empleado_seleccionado.nombre}**?")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Salario Base", f"S/. {resumen['salario_base']}")
            with col2:
                st.metric("Salario Neto", f"S/. {resumen['salario_neto']}")
            
            if st.button("Eliminar Definitivamente", key="btn_eliminar"):
                del st.session_state.empleados_ej4[indice]
                st.success("Empleado eliminado correctamente")
        else:
            st.info("No hay empleados para eliminar")
