def calcular_area(poligono, base=0, altura=0, lado=0):
    if poligono == "triangulo":
        return (base * altura) / 2
    elif poligono == "cuadrado":
        return lado * lado
    elif poligono == "rectangulo":
        return base * altura
    else:
        return "poligono no soportado"

# pruebas de cada poligono
print("Area del triangulo:", calcular_area("triangulo", base=15, altura=5))
print("Area del cuadrado:", calcular_area("cuadrado", lado=6))
print("Area del rectangulo:", calcular_area("rectangulo", base=12, altura=3))