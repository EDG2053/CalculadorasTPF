from conversiones_funciones import a_octal
from conversiones_funciones import a_binario
from conversiones_funciones import a_hexa

def Calculadora_Conversion():
    print("""
          
          ----- MENU DE CONVERSIONES -----
                1. A octal
                2. A binario
                3. A Hexadecimal
                """)
    
    opcion= int(input("Ingrese conversión: "))
    if opcion == 1:
        a_octal()
    if opcion == 2:
        a_binario()
    if opcion == 3:
        a_hexa()         
        