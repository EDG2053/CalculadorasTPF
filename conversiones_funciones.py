from func_globales import numero_valido

#CONVERSIONES (3)

def a_octal():
    
    #DECIMAL A OCTAL
    print("DECIMAL ---> OCTAL")
    num1 = input("ingrese decimal: ")
    num1 = numero_valido(num1)
    octal = "" # Asignar valor (UnboundLocalError).
    
    while num1 >= 8: # Verificacion.
        resto = num1 % 8 # Sacar resto.
        num1 = num1 // 8 # Sacar cociente.
        octal += str(resto) # Resto a Str.
    
    octal += str(num1) # Decimal a Str.
    octal = octal [::-1] #Invertir cadena.
    print(f"El octal es: {octal}")

def a_binario():
    
    #DECIMAL A BINARIO
    print("DECIMAL ---> BINARIO")
    num1 = input("Ingrese decimal: ")
    num1 = numero_valido(num1)

    binario = "" # Asignar valor (UnboundLocalError).
    
    while num1 >= 2: # Verificacion.
        resto = num1 % 2 # Sacar resto.
        num1 = num1 // 2 # Sacar cociente.
        binario += str(resto) # Resto a Str.
        
    binario += str(num1) # Decimal a Str.
    binario = binario [::-1] #Invertir cadena.
    print("El binario es", binario)

def a_hexa():
    valores_hexa = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 
                    8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    print("DECIMAL ---> HEXA")

    num1 = input("ingrese decimal: ")
    num1 = numero_valido(num1)
    
    restos = [] # Lista para restos 
    hexadecimales = "" # Guardar valores hexa.
    while num1 >= 16:
        
        resto = num1 % 16 # Sacar resto. 
        
        num1 = num1 // 16 # Sacar cociente.
        
        restos.append(resto) # Agregar el resto a lista restos.
        
    restos.append(num1)    
    
    for r in (restos): # Leer lista residuos.
        hexadecimales += valores_hexa[r]
        
        
        num_hexa = hexadecimales [::-1] # Join elimina corchetes y comas de la lista
        
    
    print(num_hexa)
