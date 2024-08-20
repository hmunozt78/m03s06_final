from os import system
num1 = int()
num2 = int()
num3 = int()

continuar = True

while continuar:
    system("cls")
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    num3 = int(input("Ingrese un numero: "))
    listaNumeros = [num1, num2, num3]
    listaNumeros.sort()
    print()
    print(f"Los numeros ingresados fueron: {num1}, {num2} y {num3}")
    print(f"y los numeros ordenados son {listaNumeros}")
    print()
    opcion=input("Desea Probar nuevamente? (s/n): ").lower()
    if opcion!="s":
        continuar= False

