
#
# --------- Funciones de Validaciones ---------
#

def numero_valido(num):
    try:
        float(num)
    except ValueError:
        num=input("Error, tiene que ingresar un numero:")
    else:
        num=float(num)
        if num%1 == 0:
            num=int(num)
    return num


def operador_valido(operador):
    """
        
    """


    operador= operador.strip() # strip elimina los espacios 
    operadores=["+","-","x", "/","="]        
    
    while not (operador in operadores):
        print("El operador debe ser |+|, |-|, |x|(equis), |/| o |=| ")
        operador=input("\n Reingrese operador: ")

    return operador

#
# ---------FIN de Funciones de Validaciones ---------
#

#
# --------- Func. Realizar operaciones ---------
#

def operacion(num1, operador, num2):
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

print(operador_valido(input("op: ")))