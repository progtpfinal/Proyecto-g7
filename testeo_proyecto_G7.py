from prueba import *


#testeos de pregunta 6:
#testeos de funciones de la pregunta 6 que plantea la creación 
#de un mapa y el conteo de los pacientes para dibujar los 
#graficos.

def test_contar_casos_graves():
    assert contar_casos_graves({1:{"country":"Pakistan","severity":"Mild","outcome":"Fatal"},2:{"country":"Pakistan","severity":"Mild","outcome":"Recovering"},3:{"country":"Pakistan","severity":"Mild","outcome":"Fatal"},4:{"country":"Pakistan","severity":"Moderate","outcome":"Fatal"},5:{"country":"Pakistan","severity":"Severe","outcome":"Fatal"}},"Pakistan") == (1,4)
    # assert contar_casos_graves()==
    # assert contar_casos_graves()==
    # assert contar_casos_graves()==
    # assert contar_casos_graves()==
    # assert contar_casos_graves()==    
    