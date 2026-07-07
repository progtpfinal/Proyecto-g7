import streamlit as st
import matplotlib.pyplot  as plt

#_________________________________________________________________________________________________________

#APERTURA DEL ARCHIVO

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

#_________________________________________________________________________________________________________
#FUNCIONES DE PREGUNTA 1(ESTÁTICA):
#PREGUNTA:
#¿QUÉ DÍA HUBO MÁS PERSONAS INICIANDO EL TRATAMIENTO?  
#RESOLUCIÓN:   
#NUESTRA FUNCIÓN GENERA UN GRAFICO DE BARRAS MOSTRANDO LAS DIFERENTES FECHAS CON FECHAS SALTEADAS,
#CON LAS RESPECTIVAS CANTIDADES DE PERSONAS QUE SE INGRESARON ESA FECHA DEL AÑO ALREDEDOR DEL MUNDO.


def contar_pacientes_por_fecha(pacientes:dict)->dict: #funcion refactorizada eliminacion del doble bucle
    """
    fechas de pacientes ingresados:dict
    proposito:
    nuestra función recibe un diccionario con las fechas de nuestros pacientes
    y nos devuelve un diccionario con todas las fechas ingresadas como claves en este,
    y sus respectivas cantidades de pacientes como datos de cada fecha, además
    tras obtener todas las fechas devuelve un diccionario ordenado con las fechas.
    contar_pacientes_por_fecha(
    {'PT-132440': {'age': '18', 'gender': 'Male', 'country': 'Canada', 'drug_name': 'Metformin', 'dosage_mg': '20', 'side_effect': 'Diarrhea', 'severity': 'Moderate', 'outcome': 'Hospitalized', 'report_date': '2021-10-30', 'treatment_start_date': '2021-09-12', 'chronic_condition': 'Kidney Disease', 'smoker': 'Yes', 'alcohol_use': 'Occasional', 'hospitalized': 'Yes', 'recovery_days': '', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'},
    'PT-117372': {'age': '76', 'gender': 'Female', 'country': 'Germany', 'drug_name': 'Lisinopril', 'dosage_mg': '20', 'side_effect': 'Fatigue', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2025-01-25', 'treatment_start_date': '2024-12-02', 'chronic_condition': 'Hypertension', 'smoker': 'Yes', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '33.0', 'capital_lat': '52.52', 'capital_lon': '13.405'}, 
    'PT-153905': {'age': '36', 'gender': 'Female', 'country': 'Canada', 'drug_name': 'Paracetamol', 'dosage_mg': '100', 'side_effect': 'Liver Toxicity', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2022-01-24', 'treatment_start_date': '2021-12-17', 'chronic_condition': 'Hypertension', 'smoker': 'No', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '30.0', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'}, 
    'PT-138339': {'age': '50', 'gender': 'Male', 'country': 'Pakistan', 'drug_name': 'Amoxicillin', 'dosage_mg': '250', 'side_effect': 'Diarrhea', 'severity': 'Moderate', 'outcome': 'Hospitalized', 'report_date': '2022-11-03', 'treatment_start_date': '2022-09-07', 'chronic_condition': 'Kidney Disease', 'smoker': 'Yes', 'alcohol_use': '', 'hospitalized': 'Yes', 'recovery_days': '', 'capital_lat': '33.6844', 'capital_lon': '73.0479'}
    })
    ==
    {'2021-09-12':1,'2022-09-07':1,'2021-12-17':1,'2024-12-02':1}"""
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


#_________________________________________________________________________________________________________
#FUNCIONES DE PREGUNTA 2 (DINÁMICA):
#PREGUNTA:
#¿CUALES SON LOS EFECTOS SECUNDARIOS DE CIERTOS MEDICAMENTOS?
#SOLUCIÓN:
#PARA LA RESOLUCIÓN DE ESTA PREGUNTA SE ELIGIO REPRESENTAR LA SOLUCIÓN MEDIANTE UN GRÁFICO DE TORTAS
#QUE NOS MUESTRE LOS PORCENTAJES DE CADA MEDICAMENTO, ESTE VA A PODER SER SELECCIONADO POR UNA INTERFAZ
#DONDE APARECERAN TODOS LOS MEDICAMENTOS Y AL SELECCIONAR UNO EL GRÁFICO CAMBIARA MOSTRANDO LOS EFECTOS 
#SECUNDARIOS DE ESTE.


def calcular_Porcentaje(medicamento:str,pacientes:dict)->dict:
    """
    datos reales:
    medicamento ingresado:str
    información de pacientes:dict
    proposito:
    recibe un diccionario y un medicamento y devuelve un diccionario que 
    contiene los efectos secundarios del medicamento recibido como clave
    y como valor tiene los porcentajes de cada uno de estos efectos secundarios.
    calcular_porcentaje(
    'Ibuprofen',{
    'PT-169877': {'age': '48', 'gender': 'Male', 'country': 'Germany', 'drug_name': 'Metformin', 'dosage_mg': '250', 'side_effect': 'Nausea', 'severity': 'Moderate', 'outcome': 'Recovering', 'report_date': '2023-05-11', 'treatment_start_date': '2023-05-05', 'chronic_condition': 'Kidney Disease', 'smoker': 'Yes', 'alcohol_use': 'Occasional', 'hospitalized': 'No', 'recovery_days': '27.0', 'capital_lat': '52.52', 'capital_lon': '13.405'}, 
    'PT-100457': {'age': '90', 'gender': 'Female', 'country': 'Canada', 'drug_name': 'Lisinopril', 'dosage_mg': '10', 'side_effect': 'Dizziness', 'severity': 'Moderate', 'outcome': 'Recovering', 'report_date': '2025-01-23', 'treatment_start_date': '2024-11-27', 'chronic_condition': '', 'smoker': 'No', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '6.0', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'},
    'PT-171214': {'age': '52', 'gender': 'Female', 'country': 'USA', 'drug_name': 'Insulin', 'dosage_mg': '100', 'side_effect': 'Sweating', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2021-10-30', 'treatment_start_date': '2021-10-20', 'chronic_condition': '', 'smoker': 'Yes', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '43.0', 'capital_lat': '38.9072', 'capital_lon': '-77.0369'}, 
    'PT-146920': {'age': '18', 'gender': 'Male', 'country': 'Canada', 'drug_name': 'Ibuprofen', 'dosage_mg': '20', 'side_effect': 'Heartburn', 'severity': 'Mild', 'outcome': 'Recovering', 'report_date': '2022-07-31', 'treatment_start_date': '2022-06-20', 'chronic_condition': 'Diabetes', 'smoker': 'Yes', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '29.0', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'},
    'PT-186635': {'age': '79', 'gender': 'Male', 'country': 'Canada', 'drug_name': 'Ibuprofen', 'dosage_mg': '25', 'side_effect': 'Nausea', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2024-06-22', 'treatment_start_date': '2024-06-21', 'chronic_condition': 'Hypertension', 'smoker': 'No', 'alcohol_use': 'Occasional', 'hospitalized': 'No', 'recovery_days': '9.0', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'}}
    )
    =={'Heartburn':50,'Nausea':50}

    """
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
    


def crear_grafico_torta(medicamento:str,pacientes:dict):
    """
    datos reales:
    medicamento ingresado:str
    información de pacientes:dict
    proposito:
    nos muestra por pantalla el grafico obtenido con los porcentajes de
    efectos secundarios que tiene el medicamento ingresado."""
    porcentajes = calcular_Porcentaje(medicamento, pacientes)
    lista_efectsec = list(porcentajes.keys()) #lista con los efectos secundarios
    lista_porcentaje = list(porcentajes.values()) #lista con el porcentaje
    fig, ax = plt.subplots() #crea la figura
    ax.pie(lista_porcentaje,labels=lista_efectsec,autopct='%1.1f%%')
    ax.set_title(f"Efectos secundarios de {medicamento}")
    return fig


#_________________________________________________________________________________________________________
#FUNCIONES DE PREGUNTA 3 (ESTÁTICA):
#PREGUNTA:
#¿SEGÚN LOS HÁBITOS Y CONDICIONES, DE QUE MANERA INFLUYEN EN EL ÍNDICE DE HOSPITALIZACIÓN?
#SOLUCIÓN:
#PARA RESOLVER LA PREGUNTA SE PENSO EN LA CREACIÓN DE DOS GRAFICOS DE BARRA COMPARANDO LAS CONDIONES
#DE LOS PACIENTES, EN ELLOS MOSTRANDO LA CANTIDAD DE PACIENTES CON ESAS CONDICIONES INDICANDO SI FUERON
#HOSPITALIZADAS.


def obtener_estadisticas(pacientes: dict)->tuple:
    """
    información del paciente:dict
    datos estadisticos:tuple(dict,dict):
    proposito:
    nos calcula la cantidad de pacientes con diferentes condiones de habitos
    de salud y nos muestra si fueron hospitalizados o no, devolviendo los resultados
    sin contemplar la hospitalización, como una que si la contempla, en dos diccionarios
    distintos devolviendo una tupla con estos diccionarios.
    """
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
    """datos reales:
    datos estadisticos:dict
    titulo del grafico:str
    proposito:
    grafica barras comparativas usando el diccionario recibido, como insertando un titulo
    a la grafica dibujada mostrando por pantalla las comparaciones de resultados al comparar
    los niveles de las barras y las cantidades que contienen.
    """

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

#_________________________________________________________________________________________________________
#FUNCIONES DE PREGUNTA 4 (ESTÁTICA):
#PREGUNTA:
#¿LA DOSIS SUMINISTRADA INFLUYE EN LA SEVERIDAD PRESENTADA POR EL PACIENTE?
#RESOLUCIÓN:
#PARA RESPONDER A LA PREGUNTA SE ELIGIO MOSTRAR UN GRAFICO DE DISPERSIÓN DE PUNTOS
#PARA MOSTRAR, ACORDE EL TAMAÑO DEL PUNTO, LA DOSIS SUMINISTRADA DE CADA MEDICAMENTO.


def contar_hospitalizados_por_dosis(pacientes: dict)->dict:
    """
    datos reales:
    datos de los pacientes:dict
    proposito:
    nuestra función recibe un diccionario con los pacientes, y nos calcula
    acorde el medicamento, la dosis y el estado la cantidad de personas
    que padecen de condiciones similares, verificando si esta hospitalizado
    para contarlo como valido.
    contar_hospitalizados_por_dosis({
    'PT-148763': {'age': '39', 'gender': 'Male', 'country': 'UK', 'drug_name': 'Lisinopril', 'dosage_mg': '10', 'side_effect': 'Fatigue', 'severity': 'Severe', 'outcome': 'Recovered', 'report_date': '2025-06-17', 'treatment_start_date': '2025-05-25', 'chronic_condition': 'Kidney Disease', 'smoker': 'Yes', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '5.0', 'capital_lat': '51.5074', 'capital_lon': '-0.1278'}, 
    'PT-166719': {'age': '59', 'gender': 'Female', 'country': 'Pakistan', 'drug_name': 'Insulin', 'dosage_mg': '100', 'side_effect': 'Weight Gain', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2022-07-19', 'treatment_start_date': '2022-06-01', 'chronic_condition': 'Heart Disease', 'smoker': 'Yes', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '22.0', 'capital_lat': '33.6844', 'capital_lon': '73.0479'}, 
    'PT-126322': {'age': '56', 'gender': 'Female', 'country': 'USA', 'drug_name': 'Omeprazole', 'dosage_mg': '50', 'side_effect': 'Headache', 'severity': 'Mild', 'outcome': 'Recovering', 'report_date': '2026-04-22', 'treatment_start_date': '2026-03-31', 'chronic_condition': '', 'smoker': 'Yes', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '7.0', 'capital_lat': '38.9072', 'capital_lon': '-77.0369'}, 
    'PT-106537': {'age': '52', 'gender': 'Male', 'country': 'Germany', 'drug_name': 'Omeprazole', 'dosage_mg': '10', 'side_effect': 'Fatigue', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2022-11-28', 'treatment_start_date': '2022-10-05', 'chronic_condition': '', 'smoker': 'Yes', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '43.0', 'capital_lat': '52.52', 'capital_lon': '13.405'}})
     'PT-182714': {'age': '28', 'gender': 'Male', 'country': 'India', 'drug_name': 'Lisinopril', 'dosage_mg': '250', 'side_effect': 'Dizziness', 'severity': 'Moderate', 'outcome': 'Hospitalized', 'report_date': '2023-09-06', 'treatment_start_date': '2023-08-11', 'chronic_condition': 'Asthma', 'smoker': 'Yes', 'alcohol_use': '', 'hospitalized': 'Yes', 'recovery_days': '', 'capital_lat': '28.6139', 'capital_lon': '77.209'}
    ==
    {'Lisinopril':{'250'}}"""
    
    resultados = {}

    for paciente in pacientes.values():

        medicamento = paciente["drug_name"]
        dosis = paciente["dosage_mg"]
        estado = paciente["outcome"]

        if estado == "Hospitalized":

            if medicamento not in resultados:
                resultados[medicamento] = {}

            if dosis not in resultados[medicamento]:
                resultados[medicamento][dosis] = 0

            resultados[medicamento][dosis] += 1

    return resultados

def graficar_dosis_por_medicamento(resultados: dict):
    """
    datos reales:
    diccionario con los datos de hospitalización:dict
    proposito:
    nuestra función crea en base a los resultados obtenidos de hospitalización
    por dosis un gráfico de dispersión de puntos, que en base a la cantidad de
    personas que tengan esas condiciones dado el medicamento y esa dosis el 
    tamaño del punto generado en la grafica.

    Scatter plot:
    - eje x: medicamento
    - eje y: dosis (mg)
    - color: medicamento
    - tamaño: cantidad de hospitalizados
    """

    x = []
    y = []
    colores = []
    tamanios = []

    # asignamos un color por medicamento
    lista_medicamentos = list(resultados.keys())
    cmap = plt.colormaps["tab10"]
    color_map = {
        med: cmap(i % 10)
        for i, med in enumerate(lista_medicamentos)
    }

    for medicamento, dosis_dict in resultados.items():
        for dosis, cantidad in dosis_dict.items():
            x.append(medicamento)
            y.append(dosis)
            colores.append(color_map[medicamento])
            tamanios.append(cantidad * 80)  # escala del tamaño

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        x,
        y,
        c=colores,
        s=tamanios,
        alpha=0.7,
        edgecolors="black"
    )

    ax.set_xlabel("Medicamento")
    ax.set_ylabel("Dosis (mg)")
    ax.set_title("Hospitalizados por medicamento y dosis")

    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()

    return fig

#______________________________________________________________________________________________

#FUNCIONES DE PREGUNTA 5 (DINÁMICA):

#¿LA EDAD INFLUYE EN EL ÍNDICE PROMEDIO DE RECUPERACIÓN DE LOS PACIENTES?
#SOLUCION:
#SE PENSO EN LA CREACIÓN DE UN GRÁFICO DE BARRAS QUE CAMBIE A MEDIDA QUE EN UN SLIDER
#SE SELECCIONE UNA EDAD, GENERANDO GRAFICAS COMPARATIVAS CON ESE DATO, PARA MOSTRAR
#LOS PROMEDIOS DE DÍAS DE RECUPERACIÓN QUE TIENE ESA EDAD SELECCIONADA.

def seguro(dia:str)->float:
    """
    dato reeal recibido y interpretado por la maquina:
    fechas en numeros o un guion indicando los dias:float
    proposito:
    nuestra función recibe un valor que representa una fecha y nos devuelve un numero float
    verificando si esta fecha es vacia o es un numero devolviendo 0 en caso de vacio y el mismo en
    otro caso haciendo la conversion a float.
    seguro("")==0
    seguro("14")==14
    seguro("3")==3
    seguro("")==0
    """
    if dia != '':
        respuesta = float(dia)
    else:
        respuesta = 0
    return respuesta

def guardar_datos(pacientes:dict)->dict:
    """
    datos reales interpretados en la maquina:
    datos del paciente:dict
    proposito:
    nuestra funcion toma los datos del diccionario con los datos del paciente y se queda con los volores de edad
    y dias de recuperacion del paciente, devolviendo un diccionario con las claves como edades y su promedio como valor
     dentro del diccionario, que indica los dias de recuperación. 
    guardar_datos(
    {'PT-161882': {'age': '49', 'gender': 'Male', 'country': 'UK', 'drug_name': 'Amoxicillin', 'dosage_mg': '20', 'side_effect': 'Diarrhea', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2023-09-30', 'treatment_start_date': '2023-09-17', 'chronic_condition': 'Kidney Disease', 'smoker': 'No', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '7.0', 'capital_lat': '51.5074', 'capital_lon': '-0.1278'},
      'PT-136859': {'age': '59', 'gender': 'Male', 'country': 'Canada', 'drug_name': 'Sertraline', 'dosage_mg': '25', 'side_effect': 'Insomnia', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2025-01-03', 'treatment_start_date': '2024-12-05', 'chronic_condition': 'Diabetes', 'smoker': 'Yes', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '10.0', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'}, 
    'PT-127581': {'age': '18', 'gender': 'Male', 'country': 'USA', 'drug_name': 'Sertraline', 'dosage_mg': '25', 'side_effect': 'Dry Mouth', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2024-02-19', 'treatment_start_date': '2024-01-04', 'chronic_condition': 'Hypertension', 'smoker': 'No', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '32.0', 'capital_lat': '38.9072', 'capital_lon': '-77.0369'}}
    )
    ==
    {49:7,59:10,18:32}
    """
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

def obtener_edades_y_promedios(edad:int, promedios:dict)->tuple:
    """
    datos reales pasados a la maquina:
    edad de la persona:int
    dias promedio de recuperación:dict
    valores de dias y promedios:tuple(list,list)
    proposito:
    nuestra función recibe un diccionario con los valores promedios y una edad dada,
    con esta la utiliza como clave en un recorrido para generar la lista de valores
    comparativos entre dos valores anteriores y dos posteriores, asegurandose que 
    este valor se encuentre en el diccionario para mostrar el promedio y las edades respectivas
    que compara, generando una lista con las edades que seran 5 valores, como uno con 5 valores
    de promedio.
    obtener_edades(21,{19:12,20:16,21:25,22:30,23:9})==([19,20,21,22,23],[12,16,25,30,9])
    obtener_edades(18,{18:9,19:29,20:10,21:4,22:7})==([18,19,20],[9,29,10])
    obtener_edades(90,{87:15,88:0,89:11,90:10})==([88,89,90],[0,11,10])
    obtener_edades(30,{})==([],[])
    """
    edades = []
    dias = []
    for e in range(edad - 2, edad + 3):   
        if e in promedios:             
            edades.append(e)           
            dias.append(promedios[e])     
    return edades, dias

def mostrar_grafico_recuperacion(edad,promedios):
    """
    proposito:
    nuestra funcion recibe una edad y un promedio mostrando por pantalla 
    el tiempo de recuperacion de los pacientes de la edad recibida como dos
    edades de años anteriores y posteriores en caso de no existir
    solo muestra los que contiene."""
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


#_________________________________________________________________________________________________________
#FUNCIONES DE PREGUNTA 6(DINÁMICA):
#PREGUNTA:
#¿QUÉ PAÍS ES EL QUE TIENE MÁS DENSIDAD DE EFECTOS SECUNDARIOS Y FATALES? 
#SOLUCIÓN:
#SE CONSIDERO LA CREACIÓN DE UN MAPA MUNDIAL QUE NOS MUESTRE POR PANTALLA CADA PAIS CON LOS PACIENTES MARCADOS EN EL
#MAPA, COMO UNA INTERFAZ CON LOS CASOS GRAVES Y FATALES, PUDIENDO SELECCIONAR POR MEDIO DE UAN INTERFAZ EL PAIS
#QUE SE DESEA VER EN EL MAPA, PUDIENDO TAMBIEN DESPLAZARSE POR ESTE.
#

def ubicacion_pacientes(pacientes:dict,pais:str)->list:
    """pacientes:diccionarios
       pais:str
       dado todos los pacientes y un pais devuelve una lista de dicc que tiene como clave lat y lon y 
       como valor las coordenadas del paciente de ese pais.
        ubicacion_pacientes('PT-120770': {'age': '37', 'gender': 'Male', 'country': 'UK', 'drug_name': 'Atorvastatin', 'dosage_mg': '100', 'side_effect': 'Muscle Pain', 'severity': 'Moderate', 'outcome': 'Recovered', 'report_date': '2024-04-12', 'treatment_start_date': '2024-03-28', 'chronic_condition': 'Diabetes', 'smoker': 'Yes', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '9.0', 'capital_lat': '51.5074', 'capital_lon': '-0.1278'}, 
        'PT-176074': {'age': '65', 'gender': 'Male', 'country': 'Germany', 'drug_name': 'Ibuprofen', 'dosage_mg': '10', 'side_effect': 'Nausea', 'severity': 'Moderate', 'outcome': 'Hospitalized', 'report_date': '2024-11-10', 'treatment_start_date': '2024-09-13', 'chronic_condition': 'Kidney Disease', 'smoker': 'No', 'alcohol_use': 'Occasional', 'hospitalized': 'Yes', 'recovery_days': '', 'capital_lat': '52.52', 'capital_lon': '13.405'}, 'PT-158869': {'age': '57', 'gender': 'Female', 'country': 'USA', 'drug_name': 'Sertraline', 'dosage_mg': '25', 'side_effect': 'Insomnia', 'severity': 'Moderate', 'outcome': 'Recovering', 'report_date': '2024-06-21', 'treatment_start_date': '2024-05-03', 'chronic_condition': 'Diabetes', 'smoker': 'Yes', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '3.0', 'capital_lat': '38.9072', 'capital_lon': '-77.0369'},
        'PT-116884': {'age': '31', 'gender': 'Female', 'country': 'Canada', 'drug_name': 'Amoxicillin', 'dosage_mg': '5', 'side_effect': 'Rash', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2026-04-27', 'treatment_start_date': '2026-03-07', 'chronic_condition': 'Kidney Disease', 'smoker': 'Yes', 'alcohol_use': 'Occasional', 'hospitalized': 'No', 'recovery_days': '24.0', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'}
        ,UK)
        ==
        ['51.5074','-0.1278']"""   
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
    fatales y casos severos
    contar_casos_graves(
    {'PT-171202': {'age': '18', 'gender': 'Female', 'country': 'Canada', 'drug_name': 'Ibuprofen', 'dosage_mg': '25', 'side_effect': 'Stomach Pain', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2022-10-15', 'treatment_start_date': '2022-09-21', 'chronic_condition': '', 'smoker': 'No', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '2.0', 'capital_lat': '45.4215', 'capital_lon': '-75.6972'}, 
    'PT-168852': {'age': '45', 'gender': 'Male', 'country': 'Australia', 'drug_name': 'Metformin', 'dosage_mg': '10', 'side_effect': 'Diarrhea', 'severity': 'Moderate', 'outcome': 'Recovering', 'report_date': '2024-07-03', 'treatment_start_date': '2024-06-05', 'chronic_condition': 'Diabetes', 'smoker': 'No', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '18.0', 'capital_lat': '-35.2809', 'capital_lon': '149.13'},
    'PT-109351': {'age': '47', 'gender': 'Male', 'country': 'USA', 'drug_name': 'Lisinopril', 'dosage_mg': '50', 'side_effect': 'Dizziness', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2026-03-26', 'treatment_start_date': '2026-02-02', 'chronic_condition': 'Hypertension', 'smoker': 'No', 'alcohol_use': 'Frequent', 'hospitalized': 'No', 'recovery_days': '13.0', 'capital_lat': '38.9072', 'capital_lon': '-77.0369'}, 
    'PT-154167': {'age': '71', 'gender': 'Male', 'country': 'Australia', 'drug_name': 'Lisinopril', 'dosage_mg': '250', 'side_effect': 'Fatigue', 'severity': 'Mild', 'outcome': 'Recovered', 'report_date': '2022-09-18', 'treatment_start_date': '2022-08-10', 'chronic_condition': 'Heart Disease', 'smoker': 'No', 'alcohol_use': '', 'hospitalized': 'No', 'recovery_days': '6.0', 'capital_lat': '-35.2809', 'capital_lon': '149.13'}
    },Australia)
    ==
    (0,0)"""

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


#_______________________________________________________________________________________________
#FUNCIÓN MAIN LLAMADA DE NUESTRO PROGRAMA CON TODAS LAS PREGUNTAS

def main():
    pacientes = leer_archivo()

    st.subheader("Mapa de pacientes por país")
    pais = st.selectbox("Seleccione un país",
                        ["Australia","Canada","Germany","India",
                         "Pakistan","UK","USA"])
    cordenadas_pais = ubicacion_pacientes(pacientes,pais)
    severos , fatales = contar_casos_graves(pacientes, pais)
    st.metric("Severos", severos)
    st.metric("Fatales", fatales)
    st.map(cordenadas_pais)

    st.subheader("Gráfico de tratamientos")
    fechas = contar_pacientes_por_fecha(pacientes)
    fig = mostar_grafico(fechas)
    st.pyplot(fig)

    st.subheader("Efectos secundarios por medicamento")
    medicamento = st.selectbox("Seleccione un medicamento",
        ["Amlodipine","Amoxicillin","Atorvastatin","Ibuprofen",
         "Insulin","Lisinopril","Metformin","Omeprazole",
         "Paracetamol","Sertraline"])
    fig_torta = crear_grafico_torta(medicamento,pacientes)
    st.pyplot(fig_torta)

    st.subheader("Recuperación por edad")
    promedios = guardar_datos(pacientes)
    edad = st.slider("Selecciona una edad", min_value=18, max_value=90, step=1, value=30)
    fig_recuperacion = mostrar_grafico_recuperacion(edad, promedios)
    st.pyplot(fig_recuperacion)

    st.subheader("Condiciones de todos los pacientes")
    datos_generales, datos_hospitalizados = obtener_estadisticas(pacientes)
    fig1 = graficar_barras(datos_generales,"Condiciones de todos los pacientes")
    st.pyplot(fig1)

    st.subheader("Factores presentes en pacientes hospitalizados")
    fig2 = graficar_barras(datos_hospitalizados,"Factores presentes en pacientes hospitalizados")
    st.pyplot(fig2)

    st.subheader("Pacientes hospitalizados por dosis")
    datos_dosis = contar_hospitalizados_por_dosis(pacientes)
    fig3 = graficar_dosis_por_medicamento(datos_dosis)
    st.pyplot(fig3)

if __name__=="__main__":
     main()
