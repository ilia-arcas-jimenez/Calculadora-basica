
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )

opcion = 0
while True:
    print("""
    ¿Qué quieres hacer?
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Salir
    """)
    opcion = int(input("Introduce un número: ") )     

    if opcion == 1:
        print("La suma de",n1,"+",n2,"es",n1+n2)
    elif opcion == 2:
        print("La resta de",n1,"-",n2,"es",n1-n2)
    elif opcion == 3:
        print("El producto de",n1,"*",n2,"es",n1*n2)
    elif opcion == 4:
        break
    else:
        print("Opción incorrecta")