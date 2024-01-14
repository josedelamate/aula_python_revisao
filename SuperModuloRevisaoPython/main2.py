
import os
listaAlunos = []

while True:
    print('*' * 40)
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Aluno
    2 - Excluir Aluno
    3 - Listar Alunos
    0 - Sair do menu
"""))
    os.system("cls")
    print('-' * 40)
    match menu:
        case 1:           
            dicAlunos = {
                "nome" : str(input("Informe o Nome do Aluno: ")),
                "idade" : int(input("Informe a Idade: ")),
                "turma" : str(input("Informe a Turma: ")),
                "cpf" : str(input("Informe o CPF: "))
            }
            listaAlunos.append(dicAlunos)
            print("Aluno adicionado com sucesso")
        case 2:
            for aluno in estoque:
                print(aluno)
            aluno_excluida = str(input("Digite o nome da aluno que você quer deletar: "))
            if aluno_excluida in estoque:
                posicao_do_excluido = estoque.index(aluno_excluida)
                estoque.pop(posicao_do_excluido)
            print("aluno excluída com sucesso")
        case 3:
            for p,i in enumerate(listaAlunos, start=1):
                print(f"""
                {p}º ->
                Aluno :{i['nome']}
                idade :{i['idade']}
                turma :{i['turma']}
                cpf   :{i['cpf']}             
                """)
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção inválida")

    print('-' * 40)
