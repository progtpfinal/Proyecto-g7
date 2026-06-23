import streamlit as st
import matplotlib.pyplot  as plt
def leer_archivo()->dict:
    """
    archivo.txt : datos del archivo
    proposito:
    nuestra función toma los datos del archivo linea por linea,
    con ellos toma la primer linea, tomando como referencia los datos
    separados por coma para generar la cantidad de diccionarios que 
    almacenaran los datos de cada persona, el primer diccionario toma
    como clave la identificación el segundo toma como referencia el los
    otros valores siguientes al primero como diccionarios internos, 
    esto genera como resultado final un diccionario de diccionarios
    para cada columna y fila recibida, esta función esta pensada
    para recibir archivos ordenados y separados por comas.
    
    ejemplo sencillo de una idea:
    contenido archivo:
    1_ vendedor,casas,precio,tamaño
    2_vendedor1,pequeña,5000,200M*2
    devolución:
    {vendedor1:{casas:pequeña,precio:5000,tamaño:200M*2}}
    """
    pacientes = {}

    with open("drug_side_effects_10k.csv", "r") as archivo:

        encabezados = archivo.readline().strip().split(",")

        for linea in archivo:
            valores = linea.strip().split(",")

            id_paciente = valores[0]

            datos = {}

            for i in range(1, len(encabezados)):
                datos[encabezados[i]] = valores[i]

            pacientes[id_paciente] = datos
    return pacientes

def contar_pacientes_por_fecha(pacientes:dict)->dict: 
    """
    fechas de pacientes ingresados:dict
    proposito:
    nuestra función recibe un diccionario con las fechas de nuestros pacientes
    y nos devuelve un diccionario con todas las fechas ingresadas como claves en este,
    y sus respectivas cantidades de pacientes como datos de cada fecha, además
    tras obtener todas las fechas devuelve un diccionario ordenado con las fechas.
    """
    dicc_cant_fechas = {} 

    for paciente in pacientes.values():
        fecha = paciente["treatment_start_date"]
        dicc_cant_fechas[fecha] = dicc_cant_fechas.get(fecha, 0) + 1

    return dict(sorted(dicc_cant_fechas.items()))

def mostar_grafico(fechas):
    """
    fechas:diccionario
    nos muestra por pantalla los graficos que apareceran en nuestra
    como una pantalla con los datos cargados, mostrando la 
    representación elegida para cada respusta de pregunta."""
    registros_tratamiento = {}

    for clave, valor in list(fechas.items())[::200]:
       registros_tratamiento[clave] = valor

    etiquetas = []

    for fecha in registros_tratamiento.keys():
        anio, mes, _ = fecha.split("-")
        etiquetas.append(f"{mes}/{anio}")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        range(len(registros_tratamiento)),
        registros_tratamiento.values(),
        marker="o",
        linewidth=2
    )

    ax.set_title("Inicio de Tratamientos")
    ax.set_xlabel("Fechas")
    ax.set_ylabel("Cantidades")

    ax.set_xticks(range(len(registros_tratamiento)))

    ax.set_xticklabels(
        etiquetas,
        rotation=0,
        ha="right"
    )

    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    return fig

def extraer_condiciones_pacientes(pacientes: dict):

    resultados = {
        "mujeres_cronicas": 0,
        "hombres_cronicos": 0,
        "mujeres_fumadoras": 0,
        "hombres_fumadores": 0,
        "mujeres_alcoholicas": 0,
        "hombres_alcoholicos": 0
    }

    for paciente in pacientes.values():

        es_mujer = paciente["gender"] == "Female"

        if paciente["chronic_condition"]:
            if es_mujer:
                resultados["mujeres_cronicas"] += 1
            else:
                resultados["hombres_cronicos"] += 1

        if paciente["smoker"] == "Yes":
            if es_mujer:
                resultados["mujeres_fumadoras"] += 1
            else:
                resultados["hombres_fumadores"] += 1

        if paciente["alcohol_use"] == "Frequent":
            if es_mujer:
                resultados["mujeres_alcoholicas"] += 1
            else:
                resultados["hombres_alcoholicos"] += 1

    return resultados

def analizar_hospitalizaciones(pacientes: dict) -> dict:
    """
    Calcula cuántos pacientes hospitalizados presentan
    distintos factores de riesgo.
    """

    resultados = {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    }

    for paciente in pacientes.values():

        if paciente["hospitalized"] == "Yes":

            if paciente["chronic_condition"] != "":
                resultados["Enf. Crónicas"] += 1

            if paciente["smoker"] == "Yes":
                resultados["Fumadores"] += 1

            if paciente["alcohol_use"] == "Frequent":
                resultados["Alcohol Frecuente"] += 1

    return resultados

def graficar_hospitalizaciones(datos: dict):
    """
    Genera un gráfico de barras con los factores
    asociados a la hospitalización.
    """

    categorias = list(datos.keys())
    cantidades = list(datos.values())

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(categorias, cantidades)

    ax.set_title(
        "Factores presentes en pacientes hospitalizados"
    )

    ax.set_xlabel("Factor de riesgo")
    ax.set_ylabel("Cantidad de hospitalizados")

    plt.xticks(rotation=20)

    plt.tight_layout()

    return fig

def graficar_condiciones(datos: dict):
    """
    datos: dict
    Recibe un diccionario con estadísticas de pacientes y
    devuelve una figura de matplotlib con un gráfico de barras.
    """

    categorias = list(datos.keys())
    cantidades = list(datos.values())

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(categorias, cantidades)

    ax.set_title("Condiciones de los pacientes")
    ax.set_xlabel("Categorías")
    ax.set_ylabel("Cantidad")

    ax.set_xticklabels(categorias, rotation=45, ha="right")

    plt.tight_layout()

    return fig

def ubicacion_pacientes(pacientes,pais):
    """pacientes:diccionarios
       pais:str
       dado todos los pacientes y un pais devuelve una lista de dicc que tiene como clave lat y lon y 
       como valor las coordenadas del paciente de ese pais """

    cordenadas = []
    for paciente in pacientes.values():
        if paciente["country"] == pais:

            cordenadas.append({"lat" : float(paciente["capital_lat"]),
                           "lon" : float(paciente["capital_lon"])})
    
    return cordenadas

def contar_casos_graves(pacientes, pais):
    """
    datos del paciente:dict
    pais origen:str
    nuestra función recibe el diccionario y se queda con los 
    valores de pais severidad y recuperación del paciente,
    con estos calcula dado el pais recibido por la selección
    del usuario devolviendo una tupla con la cantidad de casos
    fatales y casos severos"""

    severos = 0
    fatales = 0

    for paciente in pacientes.values():

        if paciente["country"] == pais:

            if paciente["severity"] == "Severe":
                severos += 1

            if paciente["outcome"] == "Fatal":
                fatales += 1

    return severos, fatales

def main():
    pacientes = leer_archivo()

    fechas = contar_pacientes_por_fecha(pacientes)
    fig = mostar_grafico(fechas)

    condiciones = extraer_condiciones_pacientes(pacientes)
    fig_condiciones = graficar_condiciones(condiciones)

    hospitalizaciones = analizar_hospitalizaciones(pacientes)
    fig_hospitalizaciones = graficar_hospitalizaciones(hospitalizaciones)

    
    pais = st.selectbox(
        "selecione un pais",
        ["Australia", "Canada", "Germany", "India",
         "Pakistan", "UK", "USA"]
    )

    cordenadas_pais = ubicacion_pacientes(pacientes, pais)

    severos, fatales = contar_casos_graves(pacientes, pais)


    col1, col2, col3 = st.columns(3)
    with col1:

        st.subheader(f"Información de {pais}")

        st.metric("Severos", severos)
        st.metric("Fatales", fatales)
        st.map(cordenadas_pais)

    with col2:

        st.subheader("Inicio de Tratamientos")
        st.pyplot(fig)

        st.subheader("Condiciones Generales")
        st.pyplot(fig_condiciones)

    with col3:

        st.subheader(
        "Hospitalización y Factores de Riesgo")

        st.pyplot(fig_hospitalizaciones)

if __name__=="__main__":
    main()