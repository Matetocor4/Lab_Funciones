def main():
  print("Hello teacher!")

if __name__ == "__main__":
    main()

# Para adicionar numeros
def addmultiplenumbers(numbers):
    return sum(numbers)

# Para multiplicar numeros
def multiplymultiplenumbers(numbers):
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result

# Para verificar si un numero es par
def isiteven(num):
    if isinstance(num, int) or (isinstance(num, float) and num.is_integer()):
        return int(num) % 2 == 0
    return False

# Para verificar si un numero es entero
def isitaninteger(num):
    if isinstance(num, int):
        return True
    elif isinstance(num, float):
        return num.is_integer()
    else:
        return False

# Elejir opcion del menu
def calculadora_menu():
    print("CALCULADORA MEJORADA")
    print("1. Sumar múltiples números")
    print("2. Multiplicar múltiples números")
    print("3. Verificar si un número es par")
    print("4. Verificar si un número es entero")

# Para obtener una lista de numeros
def obtener_lista_numeros():
    while True:
        try:
            entrada = input("Ingresa números separados por comas (ej: 1,2,3,4): ")
            numeros = [float(num.strip()) for num in entrada.split(',')]
            return numeros
        except ValueError:
            print("Error: Por favor ingresa números válidos separados por comas.")

# Para obtener un solo numero
def obtener_numero():
    while True:
        try:
            numero = float(input("Ingresa un número: "))
            return numero
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

def main():
    print("¡Bienvenido a la calculadora mejorada!")
    
    while True:
        calculadora_menu()
        
        try:
            opcion = input("Selecciona una opción (1-5): ")
            
            if opcion == "1":
                print("\n--- SUMA DE MÚLTIPLES NÚMEROS ---")
                numeros = obtener_lista_numeros()
                resultado = addmultiplenumbers(numeros)
                print(f"La suma de {numeros} es: {resultado}")
                
            elif opcion == "2":
                print("\n--- MULTIPLICACIÓN DE MÚLTIPLES NÚMEROS ---")
                numeros = obtener_lista_numeros()
                resultado = multiplymultiplenumbers(numeros)
                print(f"El producto de {numeros} es: {resultado}")
                
            elif opcion == "3":
                print("\n--- VERIFICAR SI ES PAR ---")
                numero = obtener_numero()
                resultado = isiteven(numero)
                if resultado:
                    print(f"{numero} es un número entero par.")
                else:
                    print(f"{numero} NO es un número entero par.")
                    
            elif opcion == "4":
                print("\n--- VERIFICAR SI ES ENTERO ---")
                numero = obtener_numero()
                resultado = isitaninteger(numero)
                if resultado:
                    print(f"{numero} es un número entero.")
                else:
                    print(f"{numero} NO es un número entero.")
                    
            elif opcion == "5":
                print("¡Gracias por usar la calculadora! ¡Hasta luego!")
                break
                
            else:
                print("Opción no válida. Por favor selecciona 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

    
 
