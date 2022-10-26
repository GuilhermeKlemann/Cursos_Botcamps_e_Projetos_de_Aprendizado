# Old Style #

nome = "Guilherme"
idade = 24
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao,  linguagem))
# %s = string; %d = valores inteiros; %f = valores com ponto flutuante #


# Método format #

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como{} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))
# print("Olá, me chamo nome {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))


# f-string #

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# formatando strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")  # .2f Exibe apenas 2 casas decimais #
print(f"Valor de PI: {PI:10.2f}") # 10.2f Exibe 10 caracteres (deixando os não preenchidos em espaços em branco) e exibe apenas 2 casas decimais #
