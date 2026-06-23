from prueba import *


#testeos de pregunta 6:
#testeos de funciones de la pregunta 6 que plantea la creación 
#de un mapa y el conteo de los pacientes para dibujar los 
#graficos.

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

