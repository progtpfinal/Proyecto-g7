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

def fecha_tratamiento_pacientes():
    fechas=[]
    pacientes=leer_archivo() #data_set (representado con un diccionario de diccionario)
    for i in pacientes.values():#cada valor i es el valor del diccionario
        fechas.append(i["treatment_start_date"])#agrega la fecha de cada dicc a la lista 
        fechas.sort()#ordenamos las fechas de menor a mayor
        dicc_cant_fecha={} 
        for fecha in fechas:
            dicc_cant_fecha[fecha]=dicc_cant_fecha.get(fecha,0)+1
    return (dicc_cant_fecha) 



