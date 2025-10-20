def verificar_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(frase)

if resultado:
    print("Sim")
else:
    print("Não")


text = input()

verificar_palindromo(text)

