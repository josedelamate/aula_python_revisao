import os
clear = lambda: os.system('cls') #Função Lambda - Limpar console
estoque = []

def adicionar_fruta():
            nome_fruta = str(input("Digite o nome da fruta: "))

            while True:
                try:
                    quantidade_fruta = int(input("Digite a quantidade de frutas no estoque: "))
                    if quantidade_fruta >= 1:
                        break
                    else:
                        print("Digite um valor positivo")
                except ValueError:
                     print("ERROR, digite um valor válido")
                
            while True:
                try:
                    preco_fruta = float(input("Digite o preço da fruta: "))

                    if preco_fruta > 0:
                        break
                    else:
                        print("Insira um valor válido")
                except ValueError:
                     print("ERROR, digite um valor válido")

            dicionario_fruta = {
                "Nome": nome_fruta,
                "Quantidade": quantidade_fruta,
                "Preço": preco_fruta
            }

            estoque.append(dicionario_fruta)
            return "Fruta adicionada com sucesso"


def deletar_fruta():
            visualizar_frutas()
            try:
                posicao_excluida = int(input("Digite o número da fruta que você quer deletar: "))
                if posicao_excluida >= 0 and posicao_excluida < len(estoque):
                    estoque.pop(posicao_excluida)
                    return "Fruta excluída com sucesso"
                else:
                    return "Por Favor, Digite uma posição dentro da lista que eu mostrei"
            except ValueError:
                 print("ERROR, digite um valor válido")

def deletar_nome():
    visualizar_frutas()                
    try:
        print("Você está excluindo uma fruta")
        op = str(input('Digite a Fruta para retirar da Lista: ')).lower().strip()    
        exist = False
        posicao = -1
        for pos, fruta in enumerate(estoque):
            if fruta["Nome"] == op:
                posicao = pos
                exist = True
        if exist :
            deletado = estoque.pop(posicao)
            print(f'fruta excluida = {deletado}')
        else:
            print(f'fruta não encontrada ! = {op}')    
    except ValueError:
        print("ERROR, digite um valor válido")  

def select_fruta():
            selec = int(input("""
                Escolha uma opção para atualizar
                1 - Quantidade da Fruta em Estoque
                2 - Preço da Fruta em Estoque
                0 - Voltar ao Menu Principal
            """))
            clear()
            if selec in (1,2): 
                visualizar_frutas()
                try:
                    posicao_select = int(input("Digite o número da fruta que você quer Deseja Atualizar: "))
                    if posicao_select >= 0 and posicao_select < len(estoque):
                        if selec == 1:
                            estoque[posicao_select]["Quantidade"] = int(input("Digite o nova Quantidade da fruta para Atualizar: "))
                        elif selec == 2:     
                            estoque[posicao_select]["Preço"] = float(input("Digite o novo Preço da fruta para Atualizar: "))
                         
                        return "Fruta Atualizada com sucesso"
                    else:
                        return "Por Favor, Digite uma posição dentro da lista que eu mostrei"
                except ValueError:
                    print("ERROR, digite um valor válido")
            else: 
                "Voltando ao Menu Principal..."        

def visualizar_frutas():
    for posicao,fruta in enumerate(estoque):
        print(f'{posicao} -> Fruta:{fruta["Nome"]} | Qtd:{fruta["Quantidade"]} | Preço:{fruta["Preço"]} ') 


while True:
    try:
        menu = int(input("""
        Escolha uma opção
        1 - Adicionar Fruta
        2 - Excluir Fruta
        3 - Ver todas as Frutas
        4 - Editar Fruta
        0 - Sair do menu
    """))
        clear()
        match menu:
            case 1:
                print(adicionar_fruta())
            case 2:
                opcao = int(input("""
                    Escolha uma opção de Excluir Fruta
                    1 - Por código
                    2 - Por Nome
                    0 - Voltar do menu
                """))
                clear()
                if (opcao == 1):                     
                    print(deletar_fruta())
                elif (opcao == 2):    
                   deletar_nome() 
                else:
                   print('Voltando ao Menu Principal...')      
            case 3:
                visualizar_frutas()
            case 4:
                select_fruta()
            case 0:
                print("Fim do programa")
                break
            case _:
                print("Opção inválida")
    except ValueError:
         print(f"ERROR: Digite um valor válido")