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

    ax.fill_between(
        range(len(registros_tratamiento)),
        registros_tratamiento.values(),
        alpha=0.3
    )

    ax.set_title(
        "Evolución del Inicio de Tratamientos",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Fecha")
    ax.set_ylabel("Cantidad de pacientes")

    ax.set_xticks(range(len(registros_tratamiento)))
    ax.set_xticklabels(etiquetas, rotation=45)

    ax.grid(True, linestyle="--", alpha=0.4)

    # Mostrar valores sobre cada punto
    for i, valor in enumerate(registros_tratamiento.values()):
        ax.text(i, valor + 1, str(valor), ha="center")

    plt.tight_layout()

    return fig

def obtener_estadisticas(pacientes: dict):

    resultados = {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    }

    hospitalizados = {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    }

    for paciente in pacientes.values():

        estadisticas = {
            "Enf. Crónicas": paciente["chronic_condition"] != "",
            "Fumadores": paciente["smoker"] == "Yes",
            "Alcohol Frecuente": paciente["alcohol_use"] == "Frequent"
        }

        for categoria, cumple_condicion in estadisticas.items():

            if cumple_condicion:
                resultados[categoria] += 1

                if paciente["hospitalized"] == "Yes":
                    hospitalizados[categoria] += 1

    return resultados, hospitalizados

def graficar_barras(datos: dict, titulo: str):  

    categorias = list(datos.keys())
    cantidades = list(datos.values())

    fig, ax = plt.subplots(figsize=(8, 5))

    barras = ax.bar(
        categorias,
        cantidades,
        color=["#4C72B0", "#55A868", "#C44E52"]
    )

    # Agrega el valor arriba de cada barra
    for barra in barras:
        altura = barra.get_height()

        ax.text(
            barra.get_x() + barra.get_width()/2,
            altura + 5,
            f"{int(altura)}",
            ha="center"
        )

    ax.set_title(
        titulo,
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Categorías")
    ax.set_ylabel("Cantidad de pacientes")

    ax.grid(axis="y", linestyle="--", alpha=0.4)

    plt.xticks(rotation=15)

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
    
    pais = st.selectbox(
        "selecione un pais",
        ["Australia", "Canada", "Germany", "India",
         "Pakistan", "UK", "USA"]
    )

    cordenadas_pais = ubicacion_pacientes(pacientes, pais)
    severos, fatales = contar_casos_graves(pacientes, pais)

    
    datos_generales, datos_hospitalizados = obtener_estadisticas(pacientes)
    fig1 = graficar_barras(datos_generales,"Condiciones de todos los pacientes")
    fig2 = graficar_barras(datos_hospitalizados,"Factores presentes en pacientes hospitalizados")


    col1, col2, col3 = st.columns(3)
    with col1:

        st.subheader(f"Información de {pais}")

        st.metric("Severos", severos)
        st.metric("Fatales", fatales)
        st.map(cordenadas_pais)

    with col2:

        st.subheader("Inicio de Tratamientos")
        st.pyplot(fig)


    with col3: 
        st.pyplot(fig1)
        st.pyplot(fig2)

if __name__=="__main__":
    main()