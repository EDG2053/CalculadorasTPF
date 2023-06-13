from func_globales import numero_valido as num_val
from clasica import Calculadora_Clasica 
from fraccion import Calculadora_fracciones
from conversion import a_hexa, a_binario, a_octal

print("""
    Para una mejor experiencia le sugerimos 
        expandir el tamaño de la terminal
    
        ---- MENU CALCULADORAS ----

                1 - Clasica
                2 - Fracciones 
                3 - Conversiones
                4 - Salir / off

    """)
opcion= num_val( input("     Ingrese el numero de calculadora:  ") )

while opcion !=4:
    if opcion == 1:
        Calculadora_Clasica()
    elif opcion == 2:
        Calculadora_fracciones()
    elif opcion == 3:
        pass

    print("""   
        ---- MENU CALCULADORAS ----

                1 - Clasica
                2 - Fracciones 
                3 - Conversiones
                4 - Salir / off
    """)

    opcion= num_val( input("     Ingrese el numero de calculadora:  ") )
    