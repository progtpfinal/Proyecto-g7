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
    cordenadas = []
    

    for paciente in pacientes.values():
        if paciente["country"] == pais:

            cordenadas.append({"lat" : float(paciente["capital_lat"]),
                           "lon" : float(paciente["capital_lon"])})
    
    return cordenadas

def contar_casos_graves(pacientes, pais):

    severos = 0
    fatales = 0

    for paciente in pacientes.values():

        if paciente["country"] == pais:

            if paciente["severity"] == "Severe":
                severos += 1

            elif paciente["outcome"] == "Fatal":
                fatales += 1

    return severos, fatales

def main():
    pacientes = leer_archivo()

    fechas = contar_pacientes_por_fecha(pacientes)
    fig = mostar_grafico(fechas)

    pais = st.selectbox("selecione un pais",
                        ["Australia","Canada","Germany","India",
                         "Pakistan","UK","USA"])
    
    cordenadas_pais = ubicacion_pacientes(pacientes,pais)
    
    severos , fatales = contar_casos_graves(pacientes, pais)

    col1, col2 = st.columns(2)#considerar hacerlo por pestanias 
    with col1:

        st.subheader("Información de ",pais)

        st.metric("Severos", severos)

        st.metric("Fatales", fatales)

    st.map(cordenadas_pais)

    with col2:
        st.subheader("Grafico")
        st.pyplot(fig)
    
if __name__=="__main__":
    main()