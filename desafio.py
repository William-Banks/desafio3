inventario = []
produto = []
import os

while True:
    print()
    print(3*"-", "Menu de Gerenciamento de Inventário", 3*"-")
    print("1. Adicionar novo produto.")
    print("2. Atualizar quantidade de produtos.")
    print("3. Listar produtos.")
    print("4. Valor do estoque.")
    print("5. Sair.")
    print(43*"-")

    opcao = int(input("Digite a opção desejada: "))
    os.system("cls")

    if(opcao == 1):
        nome = input("Digite o nome do produto que deseja adicionar: ").lower()
        quantidade = int(input("Digite a quantidade dele que gostaria de adicionar: "))
        preco = float(input("Digite o preço de uma unidade do produto: "))
        print(f"O produto {nome} foi adicionado ao estoque.")
        produto.append([nome, quantidade, preco])
        inventario.append(produto)

    elif(opcao == 2):
        nome = input("Digite o nome do produto que deseja atualizar: ")
        nova_quantidade = int(input("Digite a nova quantidade: "))

        encontrado = False

        for produto in inventario:
            if produto[0] == nome:
                produto[1] = nova_quantidade
                print(f"Quantidade do produto {nome} atualizada para {nova_quantidade}")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif(opcao == 3):
        if len(inventario) == 0:
            print("O inventário está vazio")
        else:
            print("Produtos no inventário:")
            for produto in inventario:
                print(f"Nome: {produto[0]} | Quantidade: {produto[1]} | Preço: {produto[2]}")

    elif(opcao == 4):
        valor_total = 0
        for produto in inventario:
            valor_total += produto[1] * produto[2]
        print(f"Valor total do inventário é: R${valor_total}")

    elif(opcao == 5):
        print("Saindo do sistema...")
        break