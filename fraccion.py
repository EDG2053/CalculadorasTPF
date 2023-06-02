from func_globales import numero_valido, operador_valido, operacion

def pedir_fracc()->tuple:
    """
        Pide el numerador y denominador 
        Verifica que ambos sean numeros validos, si no lo son los vuelve a pedir 

        Luego toma el largo del numero con mas digitos y lo guarda para el ancho de la barra 
        
        Retorna una tupla con el siguiente orden:
        (numerador, denominador, ancho de barra)  
    """
    numerador= input("ingrese el numerador: ")
    numerador= numero_valido(numerador)

    denominador= input("ingrese el denominador")
    denominador=numero_valido(denominador)

    ancho_barra=len(str(numerador)) #La barra es la que va entre el denominador y el numerador: ────

    ancho_barra= len(str(denominador)) if len(str(denominador)) > ancho_barra else ancho_barra
    #El ancho de barra va ser igual al largo del denominador si este es mayor al largo del numerador
    
    return (numerador, denominador, ancho_barra)

def operar_fracciones(fracc1, operador, fracc2):
    """
    """
    pass


def UI_fraccion(fracc1, oper, fracc2, result):

    print(f"""
        Casio
        --- Calculadora de FRACCIONES ---       
                        
                    



         |1| |2| |3|      |+| |-| 

         |4| |5| |6|      |x| |/|

         |7| |8| |9|      |=|  

         |.| |0|
    """)

def Calculadora_fracciones():
    pass