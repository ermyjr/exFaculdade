# função hortifrutis: realiza o cadastro de produtos com seus preços
def hortifrutis():
    # lê a quantidade de produtos a serem cadastrados
    quantidade = int(input())
    # dicionário para armazenar os produtos e seus preços
    produtos = {}
    # laço para cadastrar os produtos
    for i in range(quantidade):
        # lê o nome do produto e converte para minúsculo
        nome = input().lower()
        # lê o preço do produto
        preco = float(input())
        # verifica se o produto já foi cadastrado
        if nome in produtos:
            # se já foi cadastrado, imprime mensagem de aviso
            print("Produto já cadastrado")
        else:
            # se não foi cadastrado, adiciona ao dicionário de produtos
            produtos[nome] = preco
    # retorna o dicionário de produtos
    return produtos

# função preço: consulta o preço de produtos cadastrados
def preço(produtos):
    # laço para consultar os preços
    while True:
        # lê o nome do produto e converte para minúsculo
        nome = input().lower()
        # verifica se a consulta deve ser encerrada
        if nome == "fim":
            break
        elif nome in produtos:
            # se o produto está cadastrado, imprime o preço
            print(produtos[nome])
        else:
            # se o produto não está cadastrado, imprime mensagem de aviso
            print("Produto não cadastrado")

# programa principal
# cadastra os produtos e seus preços
produtos = hortifrutis()
# consulta os preços dos produtos cadastrados
preço(produtos)