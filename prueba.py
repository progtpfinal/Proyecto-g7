import streamlit as st
import matplotlib.pyplot  as plt
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

def contar_pacientes_por_fecha(pacientes): #funcion refactorizada eliminacion del doble bucle
    """

    """

    dicc_cant_fechas = {} 

    for paciente in pacientes.values():
        fecha = paciente["treatment_start_date"]
        dicc_cant_fechas[fecha] = dicc_cant_fechas.get(fecha, 0) + 1

    return dict(sorted(dicc_cant_fechas.items()))


def mostar_grafico(fechas):

    primer_mes = {}

    for clave, valor in list(fechas.items())[::200]:#tomamos las 10 primeras fehcas usando las slicings y el cambio de tipo.
        primer_mes[clave] = valor

    fig, ax = plt.subplots()

    ax.plot(primer_mes.keys(), 
            primer_mes.values(), 
            marker="o")  
    ax.set_title("Inicio de Tratamientos")
    ax.set_xlabel("Fechas")
    ax.set_ylabel("cantidad")

    return fig
    


def main():
    pacientes = leer_archivo()
    fechas = contar_pacientes_por_fecha(pacientes)
    fig = mostar_grafico(fechas)

    st.pyplot(fig)
    
if __name__=="__main__":
    main()