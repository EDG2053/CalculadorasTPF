from func_globales import numero_valido as num_val
from clasica import Calculadora_Clasica 
from fraccion import Calculadora_fracciones
import conversion

print("""
    Para una mejor experiencia le sugerimos 
        expandir el tamaño de la terminal
    
        ---- MENU CALCULADORAS ----

                1 - Clasica
                2 - Fracciones 
                3 - COnversiones
                4 - Salir / off

    """)
opcion= num_val( input("     Ingrese el numero de calculadora:  ") )


