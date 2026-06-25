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

def contar_pacientes_por_fecha(pacientes:dict)->dict: #funcion refactorizada eliminacion del doble bucle
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
            elif paciente["outcome"] == "Fatal":
                    fatales += 1
    return severos, fatales




def calcular_Porcentaje(medicamento,pacientes):
    total=0 #cant de pacientes que tomaron ese medicamento
    efectos={}#un dicc tiene como clave los efectos secund y como valor la cant de pacientes con ese efecto secund  
    for paciente in pacientes.values():
        if paciente["drug_name"]==medicamento:
            total=total+1
            efecto=paciente["side_effect"]#guardamos en una variable el efect secundario de ese paciente 
            if not efecto in efectos:
                efectos[efecto]=1 #si no esta lo agrego como clave y al valor lo inicializo en 1
            else:
                efectos[efecto]+=1 
    for efecto in efectos:
        efectos[efecto]=efectos[efecto]*100/total #modificamos el valor donde va a tener como valor el porcentaje de ese efecto (cant personas con ese efecto *100/total de personas con ese medicamento)
    
    return efectos #devuelve un dicc que tiene como clave los efectos secund y como valor su porcentaje 
    



def crear_grafico_torta(medicamento):
    pacientes = leer_archivo()
    porcentajes = calcular_Porcentaje(medicamento, pacientes)
    lista_efectsec = list(porcentajes.keys()) #lista con los efectos secundarios
    lista_porcentaje = list(porcentajes.values()) #lista con el porcentaje
    fig, ax = plt.subplots() #crea la figura
    ax.pie(lista_porcentaje,labels=lista_efectsec,autopct='%1.1f%%')
    ax.set_title(f"Efectos secundarios de {medicamento}")
    return fig

#funciones resolucion 5:

def seguro(dia):
    if dia != '':
        respuesta = float(dia)
    else:
        respuesta = 0
    return respuesta



def guardar_datos():
    pacientes = leer_archivo()
    dicc_cant_fechas = {}

    for paciente in pacientes.values():
        edad = int(paciente["age"])
        dias = seguro(paciente["recovery_days"])

        if edad not in dicc_cant_fechas:
            dicc_cant_fechas[edad] = {"suma_dias": 0, "contador": 0}

        dicc_cant_fechas[edad]["suma_dias"] += dias
        dicc_cant_fechas[edad]["contador"] += 1
    for promedios in dicc_cant_fechas:
        dicc_cant_fechas[promedios] =  dicc_cant_fechas[promedios]["suma_dias"]//dicc_cant_fechas[promedios]["contador"]
    return dict(sorted(dicc_cant_fechas.items()))


def obtener_edades_y_promedios(edad, promedios):
    """
    Devuelve dos listas:
    - edades: la edad seleccionada ±2 (si existen en el diccionario)
    - dias: los promedios correspondientes a esas edades
    """
    edades = []
    dias = []
    for e in range(edad - 2, edad + 3):   
        if e in promedios:             
            edades.append(e)           
            dias.append(promedios[e])     
    return edades, dias



def mostrar_grafico_recuperacion(edad,promedios):
    edades,dias = obtener_edades_y_promedios(edad,promedios)

    fig, ax = plt.subplots()
    ax.bar(edades, dias, color="#32CD32")

    
    ax.bar(edad, promedios[edad], color="#DC143C")

    ax.set_facecolor("#708090")   
    fig.patch.set_facecolor("#191970")   

    ax.set_title(f"Promedio de días de recuperación: edad {edad}",color="white")
    ax.set_xlabel("Edad",color="white")
    ax.set_ylabel("Promedio de días",color="white")
    ax.set_ylim(14, 30)
    return fig

def main():
    pacientes = leer_archivo()

    fechas = contar_pacientes_por_fecha(pacientes)
    fig = mostar_grafico(fechas)

    pais = st.selectbox("Seleccione un país",
                        ["Australia","Canada","Germany","India",
                         "Pakistan","UK","USA"])
    medicamento = st.selectbox("Seleccione un medicamento",
        ["Amlodipine","Amoxicillin","Atorvastatin","Ibuprofen",
         "Insulin","Lisinopril","Metformin","Omeprazole",
         "Paracetamol","Sertraline"])

    fig_torta = crear_grafico_torta(medicamento)
    cordenadas_pais = ubicacion_pacientes(pacientes,pais)
    severos , fatales = contar_casos_graves(pacientes, pais)

    #Llamado de funciones de resolucion de pregunta 5:

    promedios = guardar_datos()
    edad = st.slider("Selecciona una edad", min_value=18, max_value=90, step=1, value=30)
    fig_recuperacion = mostrar_grafico_recuperacion(edad, promedios)

    #cuadros en nuestro diseño de pagina
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader(f"Información de {pais}")
        st.metric("Severos", severos)
        st.metric("Fatales", fatales)
        st.map(cordenadas_pais)

    with col2:
        st.subheader("Gráfico de tratamientos")
        st.pyplot(fig)

    with col3:
        st.subheader("Efectos secundarios")
        st.pyplot(fig_torta)

    with col4:
        st.subheader("Recuperación por edad")
        st.pyplot(fig_recuperacion)

if __name__=="__main__":
    main()
