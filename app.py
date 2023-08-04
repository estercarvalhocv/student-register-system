listaRA = []
listaAluno = []
listaCod = []
listaDisciplina = []
listaRA_mat = []
listaCod_mat = []
listaNota1 = []
listaNota2 = []

def relatorio_aprovados():
    # Requisito G
    codigo = input("Qual o codigo da disciplina: ")
    for index, cod in enumerate(listaCod_mat):
        if cod == codigo:
            media = (listaNota1[index] + listaNota2[index]) / 2
            if media >= 6.0:
                ra_aluno = listaRA_mat[index]
                nome_aluno = listaAluno[listaRA.index(ra_aluno)]
                print(f"Aluno: {ra_aluno} - {nome_aluno} | Aprovado")

def relatorio_reprovados():
    # Requisito F
    for index, cod in enumerate(listaCod_mat):
        media = (listaNota1[index] + listaNota2[index]) / 2
        if media < 6.0:
            ra_aluno = listaRA_mat[index]
            nome_aluno = listaAluno[listaRA.index(ra_aluno)]
            nome_disciplina = listaDisciplina[listaCod.index(cod)]
            print(f"Aluno: {ra_aluno} - {nome_aluno} | Disciplina: {nome_disciplina} | Reprovado")
            print()

def mostrar_relatorio():
    # Requisito E
    print("Listagem de Notas")
    for aluno in listaRA:
        index = listaRA.index(aluno)
        print(f"Aluno: {listaRA[index]} - {listaAluno[index]}")
        for index, cod in enumerate(listaRA_mat):
            if cod == aluno:
                print(f"Disciplina: {listaCod_mat[index]} Nota1: {listaNota1[index]} Nota2: {listaNota2[index]} Media: {(listaNota1[index] + listaNota2[index]) / 2}")

def excluir_aluno():
    #Requisito D
    aluno = input("Digite o código do aluno: ")
    if aluno in listaRA:
        try:
            index = listaRA.index(aluno)
            listaRA.pop(index)
            listaAluno.pop(index)
            for ind, cod in enumerate(listaRA_mat):
                if cod == aluno:
                    listaRA_mat.pop(ind)
                    listaCod_mat.pop(ind)
                    listaNota1.pop(ind)
                    listaNota2.pop(ind)
        except IndexError:
            print("Valor não encontrado!")
            return

def lancar_notas():
    #Requisito C
    alunoRA = input("Digite o registro do aluno: ")
    if alunoRA not in listaRA:
        print("Aluno não encontrado!")
        return
    disciplina = input("Digite o código da disciplina: ")
    if disciplina not in listaCod:
        print("Disciplina não encontrada!")
        return
    try:
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        listaRA_mat.append(alunoRA)
        listaCod_mat.append(disciplina)
        listaNota1.append(nota1)
        listaNota2.append(nota2)
    except ValueError:
        return

def cadastro_disciplina():
    # Requisito B
    codigo = input("Digite o código da disciplina: ")
    if codigo not in listaCod:
        listaCod.append(codigo)
    materia = input("Nome da Disciplina: ")
    if materia in listaDisciplina:
        print("Disciplina já existente!")
    else:
        listaDisciplina.append(materia)

def cadastro_aluno():
    # Requisito A
    alunoRA = input("Digite o registro do aluno: ")
    if alunoRA not in listaRA:
        listaRA.append(alunoRA)
    alunoNome = input("Digite o nome do aluno: ")
    if alunoNome in listaAluno:
        print("O aluno já existe")
    else:
        listaAluno.append(alunoNome)

def main():
    print("0: Sair")
    print("1: Cadastro de aluno")
    print("2: Cadastro da disciplina")
    print("3: Lançar notas 1 e 2")
    print("4: Remover aluno")
    print("5: Relatório geral")
    print("6: Relatorio aprovados por materia")
    print("7: Relatorio reprovados geral")

    option = int(input("Qual opção deseja usar: "))
    while option != 0:
        if option == 1:
            cadastro_aluno()
        elif option == 2:
            cadastro_disciplina()
        elif option == 3:
            lancar_notas()
        elif option == 4:
            excluir_aluno()
        elif option == 5:
            mostrar_relatorio()
        elif option == 6:
            relatorio_aprovados()
        elif option == 7:
            relatorio_reprovados()
        option = int(input("Qual opção deseja usar: "))

if __name__ == "__main__":
    main()
