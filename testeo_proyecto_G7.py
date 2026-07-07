from prueba_control_4 import *
#testeo de pregunta 1:

def contar_pacientes_por_fecha():
    assert contar_pacientes_por_fecha(
    {
    "PT-1": {
        "treatment_start_date": "2024-01-10"
    },
    "PT-2": {
        "treatment_start_date": "2024-01-10"
    },
    "PT-3": {
        "treatment_start_date": "2024-02-05"
    }
}
) == {
    "2024-01-10": 2,
    "2024-02-05": 1
    }
    {
    "PT-1": {
        "treatment_start_date": "2023-05-20"
    },
    "PT-2": {
        "treatment_start_date": "2022-11-01"
    },
    "PT-3": {
        "treatment_start_date": "2024-07-15"
    }}
 == {
    "2022-11-01": 1,
    "2023-05-20": 1,
    "2024-07-15": 1
}
assert contar_pacientes_por_fecha(
{
    "PT-1": {
        "treatment_start_date": "2025-03-18"
    },
    "PT-2": {
        "treatment_start_date": "2025-03-18"
    },
    "PT-3": {
        "treatment_start_date": "2025-03-18"
    },
    "PT-4": {
        "treatment_start_date": "2025-03-18"
    }
}
) == {
    "2025-03-18": 4
}
assert contar_pacientes_por_fecha(
    {
    "PT-1": {
        "treatment_start_date": "2021-12-01"
    },
    "PT-2": {
        "treatment_start_date": "2021-12-01"
    },
    "PT-3": {
        "treatment_start_date": "2020-06-15"
    },
    "PT-4": {
        "treatment_start_date": "2022-08-30"
    },
    "PT-5": {
        "treatment_start_date": "2020-06-15"
    }
}
) == {
    "2020-06-15": 2,
    "2021-12-01": 2,
    "2022-08-30": 1
    }


#testeo de preguntas 2:
assert calcular_Porcentaje(
    "Ibuprofen",
    {
        "PT-1": {"drug_name": "Ibuprofen", "side_effect": "Nausea"},
        "PT-2": {"drug_name": "Ibuprofen", "side_effect": "Heartburn"},
        "PT-3": {"drug_name": "Paracetamol", "side_effect": "Fatigue"}
    }
) == {
    "Nausea": 50.0,
    "Heartburn": 50.0
}
assert calcular_Porcentaje(
    "Amoxicillin",
    {
        "PT-1": {"drug_name": "Amoxicillin", "side_effect": "Diarrhea"},
        "PT-2": {"drug_name": "Amoxicillin", "side_effect": "Diarrhea"},
        "PT-3": {"drug_name": "Amoxicillin", "side_effect": "Diarrhea"}
    }
) == {
    "Diarrhea": 100.0
}

assert calcular_Porcentaje(
    "Metformin",
    {
        "PT-1": {"drug_name": "Metformin", "side_effect": "Nausea"},
        "PT-2": {"drug_name": "Metformin", "side_effect": "Nausea"},
        "PT-3": {"drug_name": "Metformin", "side_effect": "Fatigue"},
        "PT-4": {"drug_name": "Ibuprofen", "side_effect": "Heartburn"}
    }
) == {
    "Nausea": 66.66666666666667,
    "Fatigue": 33.333333333333336
}
assert calcular_Porcentaje(
    "Insulin",
    {
        "PT-1": {"drug_name": "Insulin", "side_effect": "Sweating"},
        "PT-2": {"drug_name": "Insulin", "side_effect": "Sweating"},
        "PT-3": {"drug_name": "Insulin", "side_effect": "Dizziness"},
        "PT-4": {"drug_name": "Insulin", "side_effect": "Fatigue"}
    }
) == {
    "Sweating": 50.0,
    "Dizziness": 25.0,
    "Fatigue": 25.0
}

#pregunta testeo 3:

assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "Diabetes",
        "smoker": "Yes",
        "alcohol_use": "Frequent",
        "hospitalized": "Yes"
    }
}
) == (
    {
        "Enf. Crónicas": 1,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    },
    {
        "Enf. Crónicas": 1,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    }
)
assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "Hypertension",
        "smoker": "No",
        "alcohol_use": "Frequent",
        "hospitalized": "No"
    },
    "PT-2": {
        "chronic_condition": "",
        "smoker": "Yes",
        "alcohol_use": "",
        "hospitalized": "No"
    }
}
) == (
    {
        "Enf. Crónicas": 1,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    },
    {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    }
)
assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "Asthma",
        "smoker": "Yes",
        "alcohol_use": "",
        "hospitalized": "Yes"
    },
    "PT-2": {
        "chronic_condition": "",
        "smoker": "Yes",
        "alcohol_use": "Frequent",
        "hospitalized": "No"
    },
    "PT-3": {
        "chronic_condition": "Diabetes",
        "smoker": "No",
        "alcohol_use": "Frequent",
        "hospitalized": "Yes"
    }
}
) == (
    {
        "Enf. Crónicas": 2,
        "Fumadores": 2,
        "Alcohol Frecuente": 2
    },
    {
        "Enf. Crónicas": 2,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    }
)
assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "",
        "smoker": "No",
        "alcohol_use": "",
        "hospitalized": "No"
    },
    "PT-2": {
        "chronic_condition": "",
        "smoker": "No",
        "alcohol_use": "Occasional",
        "hospitalized": "Yes"
    }
}
) == (
    {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    },
    {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    }
)

#testeo pregunta 4:
assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "Diabetes",
        "smoker": "Yes",
        "alcohol_use": "Frequent",
        "hospitalized": "Yes"
    }
}
) == (
    {
        "Enf. Crónicas": 1,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    },
    {
        "Enf. Crónicas": 1,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    }
)
assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "Hypertension",
        "smoker": "No",
        "alcohol_use": "Frequent",
        "hospitalized": "No"
    },
    "PT-2": {
        "chronic_condition": "",
        "smoker": "Yes",
        "alcohol_use": "",
        "hospitalized": "No"
    }
}
) == (
    {
        "Enf. Crónicas": 1,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    },
    {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    }
)
assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "Asthma",
        "smoker": "Yes",
        "alcohol_use": "",
        "hospitalized": "Yes"
    },
    "PT-2": {
        "chronic_condition": "",
        "smoker": "Yes",
        "alcohol_use": "Frequent",
        "hospitalized": "No"
    },
    "PT-3": {
        "chronic_condition": "Diabetes",
        "smoker": "No",
        "alcohol_use": "Frequent",
        "hospitalized": "Yes"
    }
}
) == (
    {
        "Enf. Crónicas": 2,
        "Fumadores": 2,
        "Alcohol Frecuente": 2
    },
    {
        "Enf. Crónicas": 2,
        "Fumadores": 1,
        "Alcohol Frecuente": 1
    }
)
assert obtener_estadisticas(
{
    "PT-1": {
        "chronic_condition": "",
        "smoker": "No",
        "alcohol_use": "",
        "hospitalized": "No"
    },
    "PT-2": {
        "chronic_condition": "",
        "smoker": "No",
        "alcohol_use": "Occasional",
        "hospitalized": "Yes"
    }
}
) == (
    {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    },
    {
        "Enf. Crónicas": 0,
        "Fumadores": 0,
        "Alcohol Frecuente": 0
    }
)

testeo 5

assert contar_hospitalizados_por_dosis(
{
    "PT-1": {
        "drug_name": "Ibuprofen",
        "dosage_mg": "20",
        "outcome": "Hospitalized"
    }
}
) == {
    "Ibuprofen": {
        "20": 1
    }
}
assert contar_hospitalizados_por_dosis(
{
    "PT-1": {
        "drug_name": "Paracetamol",
        "dosage_mg": "500",
        "outcome": "Hospitalized"
    },
    "PT-2": {
        "drug_name": "Paracetamol",
        "dosage_mg": "500",
        "outcome": "Hospitalized"
    },
    "PT-3": {
        "drug_name": "Paracetamol",
        "dosage_mg": "500",
        "outcome": "Recovered"
    }
}
) == {
    "Paracetamol": {
        "500": 2
    }
}
assert contar_hospitalizados_por_dosis(
{
    "PT-1": {
        "drug_name": "Lisinopril",
        "dosage_mg": "10",
        "outcome": "Hospitalized"
    },
    "PT-2": {
        "drug_name": "Lisinopril",
        "dosage_mg": "20",
        "outcome": "Hospitalized"
    },
    "PT-3": {
        "drug_name": "Lisinopril",
        "dosage_mg": "20",
        "outcome": "Hospitalized"
    }
}
) == {
    "Lisinopril": {
        "10": 1,
        "20": 2
    }
}
assert contar_hospitalizados_por_dosis(
{
    "PT-1": {
        "drug_name": "Insulin",
        "dosage_mg": "100",
        "outcome": "Hospitalized"
    },
    "PT-2": {
        "drug_name": "Insulin",
        "dosage_mg": "100",
        "outcome": "Recovered"
    },
    "PT-3": {
        "drug_name": "Metformin",
        "dosage_mg": "250",
        "outcome": "Hospitalized"
    },
    "PT-4": {
        "drug_name": "Metformin",
        "dosage_mg": "500",
        "outcome": "Hospitalized"
    }
}
) == {
    "Insulin": {
        "100": 1
    },
    "Metformin": {
        "250": 1,
        "500": 1
    }
}


assert guardar_datos(
{
    "PT-1": {
        "age": "20",
        "recovery_days": "10"
    },
    "PT-2": {
        "age": "30",
        "recovery_days": "20"
    },
    "PT-3": {
        "age": "40",
        "recovery_days": "30"
    }
}
) == {
    20: 10,
    30: 20,
    40: 30
}
assert guardar_datos(
{
    "PT-1": {
        "age": "25",
        "recovery_days": "8"
    },
    "PT-2": {
        "age": "25",
        "recovery_days": "12"
    },
    "PT-3": {
        "age": "40",
        "recovery_days": "20"
    }
}
) == {
    25: 10,
    40: 20
}
assert guardar_datos(
{
    "PT-1": {
        "age": "18",
        "recovery_days": "10"
    },
    "PT-2": {
        "age": "18",
        "recovery_days": "20"
    },
    "PT-3": {
        "age": "18",
        "recovery_days": "30"
    }
}
) == {
    18: 20
}
assert guardar_datos(
{
    "PT-1": {
        "age": "35",
        "recovery_days": "15"
    },
    "PT-2": {
        "age": "35",
        "recovery_days": "25"
    },
    "PT-3": {
        "age": "50",
        "recovery_days": "40"
    },
    "PT-4": {
        "age": "50",
        "recovery_days": "20"
    }
}
) == {
    35: 20,
    50: 30
}

assert obtener_edades_y_promedios(
    21,
    {
        19: 12,
        20: 16,
        21: 25,
        22: 30,
        23: 9
    }
) == (
    [19, 20, 21, 22, 23],
    [12, 16, 25, 30, 9]
)
assert obtener_edades_y_promedios(
    18,
    {
        18: 9,
        19: 29,
        20: 10,
        21: 4,
        22: 7
    }
) == (
    [18, 19, 20],
    [9, 29, 10]
)
assert obtener_edades_y_promedios(
    90,
    {
        87: 15,
        88: 0,
        89: 11,
        90: 10
    }
) == (
    [88, 89, 90],
    [0, 11, 10]
)
assert obtener_edades_y_promedios(
    30,
    {}
) == (
    [],
    []
)

assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "Canada",
        "capital_lat": "45.4215",
        "capital_lon": "-75.6972"
    },
    "PT-2": {
        "country": "USA",
        "capital_lat": "38.9072",
        "capital_lon": "-77.0369"
    }
},
"Canada"
) == [
    {
        "lat": 45.4215,
        "lon": -75.6972
    }
]
assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "Germany",
        "capital_lat": "52.52",
        "capital_lon": "13.405"
    },
    "PT-2": {
        "country": "Germany",
        "capital_lat": "52.52",
        "capital_lon": "13.405"
    },
    "PT-3": {
        "country": "Canada",
        "capital_lat": "45.4215",
        "capital_lon": "-75.6972"
    }
},
"Germany"
) == [
    {
        "lat": 52.52,
        "lon": 13.405
    },
    {
        "lat": 52.52,
        "lon": 13.405
    }
]
assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "Canada",
        "capital_lat": "45.4215",
        "capital_lon": "-75.6972"
    },
    "PT-2": {
        "country": "USA",
        "capital_lat": "38.9072",
        "capital_lon": "-77.0369"
    }
},
"India"
) == []
assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "UK",
        "capital_lat": "51.5074",
        "capital_lon": "-0.1278"
    },
    "PT-2": {
        "country": "Germany",
        "capital_lat": "52.52",
        "capital_lon": "13.405"
    },
    "PT-3": {
        "country": "UK",
        "capital_lat": "51.5074",
        "capital_lon": "-0.1278"
    }
},
"UK"
) == [
    {
        "lat": 51.5074,
        "lon": -0.1278
    },
    {
        "lat": 51.5074,
        "lon": -0.1278
    }
]


#testeos de pregunta 6:
#testeos de funciones de la pregunta 6 que plantea la creación 
#de un mapa y el conteo de los pacientes para dibujar los 
#graficos.

assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "Canada",
        "capital_lat": "45.4215",
        "capital_lon": "-75.6972"
    },
    "PT-2": {
        "country": "USA",
        "capital_lat": "38.9072",
        "capital_lon": "-77.0369"
    }
},
"Canada"
) == [
    {
        "lat": 45.4215,
        "lon": -75.6972
    }
]
assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "Germany",
        "capital_lat": "52.52",
        "capital_lon": "13.405"
    },
    "PT-2": {
        "country": "Germany",
        "capital_lat": "52.52",
        "capital_lon": "13.405"
    },
    "PT-3": {
        "country": "Canada",
        "capital_lat": "45.4215",
        "capital_lon": "-75.6972"
    }
},
"Germany"
) == [
    {
        "lat": 52.52,
        "lon": 13.405
    },
    {
        "lat": 52.52,
        "lon": 13.405
    }
]
assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "Canada",
        "capital_lat": "45.4215",
        "capital_lon": "-75.6972"
    },
    "PT-2": {
        "country": "USA",
        "capital_lat": "38.9072",
        "capital_lon": "-77.0369"
    }
},
"India"
) == []
assert ubicacion_pacientes(
{
    "PT-1": {
        "country": "UK",
        "capital_lat": "51.5074",
        "capital_lon": "-0.1278"
    },
    "PT-2": {
        "country": "Germany",
        "capital_lat": "52.52",
        "capital_lon": "13.405"
    },
    "PT-3": {
        "country": "UK",
        "capital_lat": "51.5074",
        "capital_lon": "-0.1278"
    }
},
"UK"
) == [
    {
        "lat": 51.5074,
        "lon": -0.1278
    },
    {
        "lat": 51.5074,
        "lon": -0.1278
    }
]



def test_contar_casos_graves():
    assert contar_casos_graves({1:{"country":"Pakistan","severity":"Mild","outcome":"Fatal"},
                                2:{"country":"Pakistan","severity":"Mild","outcome":"Recovering"},
                                3:{"country":"Pakistan","severity":"Mild","outcome":"Fatal"},
                                4:{"country":"Pakistan","severity":"Moderate","outcome":"Fatal"},
                                5:{"country":"Pakistan","severity":"Severe","outcome":"Fatal"}},"Pakistan") == (1,4)
    assert contar_casos_graves({1:{"country":"USA","severity":"Mild","outcome":"Fatal"},
                                2:{"country":"India","severity":"Mild","outcome":"Recovering"},
                                3:{"country":"Germany","severity":"Mild","outcome":"Fatal"},
                                4:{"country":"UK","severity":"Moderate","outcome":"Fatal"},
                                5:{"country":"Canada","severity":"Severe","outcome":"Fatal"}},"Pakistan")==(0,0)
    assert contar_casos_graves({1:{"country":"Pakistan","severity":"Mild","outcome":"Recovered"},
                                2:{"country":"Pakistan","severity":"Mild","outcome":"Recovering"},
                                3:{"country":"UK","severity":"Severe","outcome":"Fatal"},
                                4:{"country":"Pakistan","severity":"Moderate","outcome":"Fatal"},
                                5:{"country":"Pakistan","severity":"Severe","outcome":"Fatal"}},"UK")==(1,1)
    assert contar_casos_graves({1:{"country":"Pakistan","severity":"Severe","outcome":"Recovering"},
                                2:{"country":"USA","severity":"Mild","outcome":"Recovering"},
                                3:{"country":"Pakistan","severity":"Mild","outcome":"Recovering"},
                                4:{"country":"Pakistan","severity":"Moderate","outcome":"Hospitalized"},
                                5:{"country":"Pakistan","severity":"Severe","outcome":"Recoverd"}},"Pakistan")== (2,0)
    assert contar_casos_graves({1:{"country":"Canada","severity":"Moderate","outcome":"Fatal"},
                                2:{"country":"Australia","severity":"Mild","outcome":"Recovering"},
                                3:{"country":"Pakistan","severity":"Mild","outcome":"Fatal"},
                                4:{"country":"Pakistan","severity":"Moderate","outcome":"Fatal"},
                                5:{"country":"Pakistan","severity":"Severe","outcome":"Fatal"}},"Canada")==(0,1)
    assert contar_casos_graves({1:{"country":"UK","severity":"Mild","outcome":"Fatal"},
                                2:{"country":"Australia","severity":"Moderate","outcome":"Recovering"},
                                3:{"country":"Pakistan","severity":"Mild","outcome":"Fatal"},
                                4:{"country":"India","severity":"Moderate","outcome":"Fatal"},
                                5:{"country":"Pakistan","severity":"Severe","outcome":"Fatal"}},"India")==(0,1)    

