nome = "Guilherme"
idade = 24
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 24}

print("Nome:  %s Idade: %d" % (nome, idade))

print("Nome:  {} Idade: {}".format(nome, idade))

print("Nome:  {1} Idade: {0}".format(idade, nome))
print("Nome:  {nome} Idade: {idade}".format(nome = nome, idade = idade))

print("Nome:  {name} Idade: {age}".format(age = idade, name = nome))
print("Nome:  {name} Idade: {age} {name} {name} {age}".format(age = idade, name = nome))
print("Nome:  {nome} Idade: {idade}".format(**dados))

print(f"Nome:  {nome} Idade: {idade}")
print(f"Nome:  {nome} Idade: {idade} Saldo:{saldo:.1f}")
print(f"Nome:  {nome} Idade: {idade} Saldo:{saldo:10.2f}")


tempo_de_viagem = int(input().split())
velocidade = int(input().split())

consumo = float(tempo_de_viagem*velocidade/12)
print(f"{consumo:.3f}")