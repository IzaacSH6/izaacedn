
# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

x = True
notas = []

aluno = 1

while x:
    try:
        alunos = float(input(f"\nDigite a nota do aluno nº{aluno}.\nDigite 'calcular' para calcular a média \n"))
        notas.append(alunos)
        aluno += 1
    except ValueError:
        media = (sum(notas))/len(notas)
        print(f"a média das notas é: {media}")
        perg = input('Digite "parar" para sair\n')
        if perg == "parar":
            x = False
        else:
            pass

