def calcular_combustivel(distancia_percorrida, autonomia):
    combustivel_gasto = distancia_percorrida / autonomia
    return combustivel_gasto

tempo_gasto = float(input("Digite o tempo gasto pelo veículo (em horas): "))
velocidade_media = float(input("Digite a velocidade média do veículo (em km/h): "))
autonomia = float(input("Digite a autonomia do veículo (em km/l): "))

distancia_percorrida = tempo_gasto * velocidade_media
combustivel_gasto = calcular_combustivel(distancia_percorrida, autonomia)

print("A quantidade de combustível gasto foi de", combustivel_gasto, "litros.")