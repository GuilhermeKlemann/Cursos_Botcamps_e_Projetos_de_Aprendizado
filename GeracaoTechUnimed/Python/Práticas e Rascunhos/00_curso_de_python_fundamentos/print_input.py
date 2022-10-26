from turtle import end_fill


nome = input("Informe o seu nome: ")
idade = input("Informe o sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#")
print(nome, idade, sep="#", end="...\n")