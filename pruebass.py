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

def ubicacion_pacientes(pacientes,pais):
    cordenadas = []
    

    for paciente in pacientes.values():
        if paciente["country"] == pais:

            cordenadas.append({"lat" : float(paciente["capital_lat"]),
                           "lon" : float(paciente["capital_lon"])})
    
    return cordenadas

def main():
    pacientes = leer_archivo()
    

    pais = st.selectbox("selecione un pais",
                        ["Australia","Canada","Germany","India",
                         "Pakistan","UK","USA"])
    
    cordenadas_pais = ubicacion_pacientes(pacientes,pais)

    st.write("mostrando pacientes del pais ",pais)
    st.map(cordenadas_pais[:20])

if __name__=="__main__":
    main()