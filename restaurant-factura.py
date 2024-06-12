igv = 0.18
mnto = 0.0
totalfac = 0.0
cont = ""
op = 0
des = 0
alm = 0
cn = 0

print("*** RESTAURANTE PUNTO GASTRONOMICO ***")

while True:
    print("Elija una opción")
    print("(1) Desayuno ")
    print("(2) Almuerzo ")
    print("(3) Cena")

    while True:
        op = int(input())
        if op not in [1, 2, 3]:
            print("Entrada inválida")
        else:
            break

    if op == 1:
        print("Menú desayuno")
        print("(1) Té verde y tortilla de avena")
        print("(2) Café con leche ")
        print("(3) Jugo de naranja y tostadas")

        while True:
            des = int(input())
            if des not in [1, 2, 3]:
                print("Entrada inválida")
            else:
                break

    elif op == 2:
        print("Menú almuerzo")
        print("(1) Arroz con pollo")
        print("(2) Lomo saltado ")
        print("(3) Ceviche")

        while True:
            alm = int(input())
            if alm not in [1, 2, 3]:
                print("Entrada inválida")
            else:
                break

    elif op == 3:
        print("Menú cena")
        print("(1) Pan integral con queso")
        print("(2) Caldo de gallina")
        print("(3) Ensalada con atún ")

        while True:
            cn = int(input())
            if cn not in [1, 2, 3]:
                print("Entrada inválida")
            else:
                break

    print("Ingrese monto a pagar")
    mnto = float(input())

    totalfac = mnto + (mnto * igv)

    print("*** TOTAL FACTURA ***")
    print("Compra:   ", mnto)
    print("Impuesto: ", mnto * igv)
    print("Total:    ", totalfac)

    print("¿OTRA FACTURA (s/n)", end="")

    while True:
        cont = input().lower()
        if cont in ["s", "n"]:
            break

    if cont == "n":
        break
