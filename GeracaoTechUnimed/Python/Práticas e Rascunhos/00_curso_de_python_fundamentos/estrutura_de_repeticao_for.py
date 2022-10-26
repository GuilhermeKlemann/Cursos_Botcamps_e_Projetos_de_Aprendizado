# O FOR é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado.

texto = input("Informe o texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: # O ELSE executa no final do laço #
    print()
    print("Executa no final do laço")

# RANGE é uma função built-in do Python, utilizada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Ex: Se usarmos range(i,j) será produzido: i, i+1, i+2, i+3, ..., j-1. Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional) #
# Exibindo de 0 a 10 com range #
for numero in range(0, 11):
    print(numero, end=" ")
    print()

# Exibindo a tabuada do 5 com range #
for numero in range(0, 51, 5): # O 0 representa o start, o 51 o stop e o 5 as steps #
    print(numero, end= " ")