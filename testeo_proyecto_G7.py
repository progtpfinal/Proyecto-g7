from prueba_control_4 import *
#testeo de pregunta 1:

def test_contar_pacientes_por_fecha():
    assert contar_pacientes_por_fecha({
        "PT-1": {"treatment_start_date": "2024-01-10"},
        "PT-2": {"treatment_start_date": "2024-01-10"},
        "PT-3": {"treatment_start_date": "2024-02-05"}
    }) == {"2024-01-10": 2, "2024-02-05": 1}

    assert contar_pacientes_por_fecha({
        "PT-1": {"treatment_start_date": "2023-05-20"},
        "PT-2": {"treatment_start_date": "2022-11-01"},
        "PT-3": {"treatment_start_date": "2024-07-15"}
    }) == {"2022-11-01": 1, "2023-05-20": 1, "2024-07-15": 1}

    assert contar_pacientes_por_fecha({
        "PT-1": {"treatment_start_date": "2025-03-18"},
        "PT-2": {"treatment_start_date": "2025-03-18"},
        "PT-3": {"treatment_start_date": "2025-03-18"},
        "PT-4": {"treatment_start_date": "2025-03-18"}
    }) == {"2025-03-18": 4}


def test_calcular_porcentaje():
    assert calcular_Porcentaje("Ibuprofen", {
        "PT-1": {"drug_name": "Ibuprofen", "side_effect": "Nausea"},
        "PT-2": {"drug_name": "Ibuprofen", "side_effect": "Heartburn"},
        "PT-3": {"drug_name": "Paracetamol", "side_effect": "Fatigue"}
    }) == {"Nausea": 50.0, "Heartburn": 50.0}

    assert calcular_Porcentaje("Amoxicillin", {
        "PT-1": {"drug_name": "Amoxicillin", "side_effect": "Diarrhea"},
        "PT-2": {"drug_name": "Amoxicillin", "side_effect": "Diarrhea"},
        "PT-3": {"drug_name": "Amoxicillin", "side_effect": "Diarrhea"}
    }) == {"Diarrhea": 100.0}


def test_obtener_estadisticas():
    assert obtener_estadisticas({
        "PT-1": {
            "chronic_condition": "Diabetes",
            "smoker": "Yes",
            "alcohol_use": "Frequent",
            "hospitalized": "Yes"
        }
    }) == (
        {"Enf. Crónicas": 1, "Fumadores": 1, "Alcohol Frecuente": 1},
        {"Enf. Crónicas": 1, "Fumadores": 1, "Alcohol Frecuente": 1}
    )


def test_contar_hospitalizados_por_dosis():
    assert contar_hospitalizados_por_dosis({
        "PT-1": {"drug_name": "Ibuprofen", "dosage_mg": "20", "outcome": "Hospitalized"}
    }) == {"Ibuprofen": {"20": 1}}

    assert contar_hospitalizados_por_dosis({
        "PT-1": {"drug_name": "Paracetamol", "dosage_mg": "500", "outcome": "Hospitalized"},
        "PT-2": {"drug_name": "Paracetamol", "dosage_mg": "500", "outcome": "Hospitalized"},
        "PT-3": {"drug_name": "Paracetamol", "dosage_mg": "500", "outcome": "Recovered"}
    }) == {"Paracetamol": {"500": 2}}


def test_guardar_datos():
    assert guardar_datos({
        "PT-1": {"age": "20", "recovery_days": "10"},
        "PT-2": {"age": "30", "recovery_days": "20"},
        "PT-3": {"age": "40", "recovery_days": "30"}
    }) == {20: 10, 30: 20, 40: 30}


def test_obtener_edades_y_promedios():
    assert obtener_edades_y_promedios(21, {19: 12, 20: 16, 21: 25, 22: 30, 23: 9}) == (
        [19, 20, 21, 22, 23], [12, 16, 25, 30, 9]
    )


def test_ubicacion_pacientes():
    assert ubicacion_pacientes({
        "PT-1": {"country": "Canada", "capital_lat": "45.4215", "capital_lon": "-75.6972"},
        "PT-2": {"country": "USA", "capital_lat": "38.9072", "capital_lon": "-77.0369"}
    }, "Canada") == [{"lat": 45.4215, "lon": -75.6972}]



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

