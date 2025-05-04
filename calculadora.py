# Este es un programa de calculadora simple que permite al usuario realizar operaciones matemáticas básicas.
# El programa solicita al usuario que ingrese dos números y la operación deseada (+, -, *, /).
while True:
    try:
        # Solicitar al usuario que ingrese un número
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        # Solicitar al usuario que ingrese la operación deseada
        operacion = input ("Introduce la operación deseada (+, -, *, /): ")
        # Realizar la operación correspondiente
        resultado = 0
        if operacion == "+":
            resultado = num1 + num2
            print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
        elif operacion == "-":
            resultado = num1 - num2
            print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
        elif operacion == "*":
            resultado = num1 * num2
            print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
        elif operacion == "/":
            # Manejar la división por cero
            # Si el segundo número es cero, mostrar un mensaje de error
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
        else:
            print("Operación no válida. Por favor, introduce una operación válida (+, -, *, /).")
    except ValueError:
        # Si el usuario ingresa 'q', salir del bucle
        if input("¿Quieres salir? (s/n): ").lower() == 's':
            print("Saliendo del programa.")
            break
        else:
            print("Entrada no válida. Por favor, introduce un número o 'q' para salir.")


    