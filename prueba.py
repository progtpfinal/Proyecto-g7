import streamlit as st
import matplotlib as plt
def leer_archivo():
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

def fecha_tratamiento_pacientes(pacientes):
    fechas=[]  #data_set (representado con un diccionario de diccionario)
    for i in pacientes.values():#cada valor i es el valor del diccionario
        fechas.append(i["treatment_start_date"])#agrega la fecha de cada dicc a la lista 
        fechas.sort()#ordenamos las fechas de menor a mayor
        dicc_cant_fecha={} 
        for fecha in fechas:
            dicc_cant_fecha[fecha]=dicc_cant_fecha.get(fecha,0)+1
    return (dicc_cant_fecha) 


def mostar_grafico(fechas):

    fechas = fecha_tratamiento_pacientes()
    primer_mes = {}

    for clave, valor in list(fechas.items())[:10]:#tomamos las 10 primeras fehcas usando las slicings y el cambio de tipo.
        primer_mes[clave] = valor

    fig, ax = plt.subplots()
    ax.plot(primer_mes.keys(), primer_mes.values(), marker="o")  # gráfico de línea
    ax.set_title("Inicio de Tratamientos")
    ax.set_xlabel("Fechas")
    ax.set_ylabel("cantidad")

    return fig
    


def main():
    pacientes = leer_archivo()
    fechas = fecha_tratamiento_pacientes(pacientes)
    st.pyplot(mostar_grafico(fechas))
    
main()
