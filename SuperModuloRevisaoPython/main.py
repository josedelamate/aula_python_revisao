import os
estoque = []

while True:
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Fruta
    2 - Excluir Fruta
    3 - Ver todas as Frutas
    0 - Sair do menu
"""))
    os.system("cls")
    match menu:
        case 1:
            fruta_adicionada = {
                "fruta": str(input("Digite uma fruta: ")),
                "quantidade": int(input("Digite a quantidade de fruta: ")),
                "preço": str(input("Digite o preço da fruta: "))
            }
            estoque.append(fruta_adicionada)
            print("Fruta adicionada com sucesso")
        case 2:
            for i, fruta in enumerate(estoque, 1):
                print(f"{i} - {fruta['fruta']}")
            fruta_excluida = input("Digite o nome da fruta que você quer deletar: ")
            found = False
            for i, fruta in enumerate(estoque):
                if fruta['fruta'] == fruta_excluida:
                    estoque.pop(i)
                    found = True
                    print("Fruta excluída com sucesso")
            if not found:
                print("Fruta não encontrada. Nenhuma fruta foi excluída.")

        case 3:
             for i, fruta in enumerate(estoque):
                print(f""" {i+1} :{fruta['fruta']} - Quantidade: {fruta['quantidade']} - Preço: {fruta['preço']}""")

        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção inválida")
