# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.

x = True

while True:
    senha = input("Digite sua senha: ")

    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha válida.")
    else:
        print("Senha inválida. Ela deve ter pelo menos 8 caracteres e conter pelo menos um número.")
