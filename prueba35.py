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



def calcular_Porcentaje(medicamento,pacientes):
    total=0 #total de pacientes con ese medicamento
    efectos={}#tiene como clave los efectos secund y como valor la cant de pacientes con ese efecto secund  
    for paciente in pacientes.values():
        if paciente["drug_name"]==medicamento:
            total=total+1
            efecto=paciente["side_effect"]
            if not efecto in efectos:
                efectos[efecto]=1 #si no esta lo agrego 
            else:
                efectos[efecto]+=1 
    for efecto in efectos:
        efectos[efecto]=efectos[efecto]*100/total #modificamos el valor donde va a tener como valor el porcentaje de ese efecto
    
    return efectos #devuelve un dicc que tiene como clave los efectos secund y como valor su porcentaje 
    

        
def mostrar_grafico_torta():
    medicamento= st.selectbox("selecione un medicamento",["Amlodipine","Amoxicillin","Atorvastatin","Ibuprofen","Insulin","Lisinopril","Metformin","Omeprazole","Paracetamol","Sertraline"])    
    pacientes=leer_archivo()
    porcentajes=calcular_Porcentaje(medicamento,pacientes)
    lista_efectsec = list(porcentajes.keys())      # lista(str),lista de efectos secundarios
    lista_porcentaje = list(porcentajes.values())  #lista(int),lista de porcentaje
    fig, ax = plt.subplots()
    ax.pie(lista_porcentaje, labels=lista_efectsec, autopct='%1.1f%%')
    ax.set_title(f"Efectos secundarios de {medicamento}")
    st.pyplot(fig)

mostrar_grafico_torta()