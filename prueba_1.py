import streamlit as st
import matplotlib.pyplot as plt


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
        fecha = paciente["age"]
        dicc_cant_fechas[fecha] = dicc_cant_fechas.get(fecha, 0) + 1

    return dict(sorted(dicc_cant_fechas.items()))





# Datos de ejemplo
datos = {
    "Argentina": (3, 5),   # (severos, fatales)
    "Chile": (2, 1),
    "Brasil": (4, 6),
}

# Slider para elegir país
pais = st.select_slider(
    "Selecciona un país",
    options=list(datos.keys()),
    value="Argentina"
)

# Obtener valores
severos, fatales = datos[pais]

# Crear gráfico de barras
fig, ax = plt.subplots()
ax.bar(["Severos", "Fatales"], [severos, fatales], color=["orange", "red"])
ax.set_title(f"Casos en {pais}")

# Mostrar en Streamlit
st.pyplot(fig)


#labels=[irritacion,fiebre,nauseas]
#sizes = [numeros]
#sizes = [2000,5000,3000]
#sizes = [total = 10000]
#autopct="%1.1f%%"
#colors=[amarillo,rojo,azul]

ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")





