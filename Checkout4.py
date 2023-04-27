def hortifrutis():
    quantidade = int(input())
    produtos = {}
    for i in range(quantidade):
        nome = input().lower()
        preco = float(input())
        if nome in produtos:
            print("Produto já cadastrado")
        else:
            produtos[nome] = preco
    return produtos

def preço(produtos):
    while True:
        nome = input().lower()
        if nome == "fim":
            break
        elif nome in produtos:
            print(produtos[nome])
        else:
            print("Produto nao cadastrado")

produtos = hortifrutis()
preço(produtos)