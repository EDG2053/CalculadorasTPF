
#
# --------- Funciones de Validaciones ---------
#

def numero_valido(num):
    """
        Recibe un numero, si este da error al convertirlo lo vuelve a pedir hasta que 
        sea un numero.

        retorna un int si el numero no tiene decimales(.0) y float si los tiene(.3)
    """

    try:
        float(num)
    except ValueError:
        num=input("Error, tiene que ingresar un numero: ")
    else:
        num=float(num)
        if num%1 == 0:
            num=int(num)
    return num


def operador_valido(operador):
    """
        Verifica si el operador es valido ( si es +, -, x, / )
        Si no es valido lo vuelve a pedir hasta que lo sea

        retorna el operador
    """

    operador= operador.strip() # strip elimina los espacios 
    operadores=["+","-","x", "/","="]        
    
    while not (operador in operadores):
        print("El operador debe ser |+|, |-|, |x|(equis), |/| o |=| ")
        operador=input("\n Reingrese operador: ")# \n hace un salto de linea

    return operador

#
# ---------FIN de Funciones de Validaciones ---------
#

#
# --------- Func. Realizar operaciones ---------
#

def operacion(num1, operador, num2):
    """
        Realiza una operacion segun el operador que reciba( +, -, x, / )
        Retorna el resultado

        Usar solo luego de validar los numeros y operadores
    """
    sumar=operador == "+"
    restar=operador == "-"
    dividir=operador == "/"
    multiplicar=operador == "x"
    resultado=0

    if sumar:
        resultado= num1+num2
    elif restar:
        resultado= num1-num2
    elif dividir:
        resultado= num1/num2
    elif multiplicar:
        resultado= num1*num2

    return resultado

#
# ---------FIN Func. de Realizar operaciones ---------
#

