# Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. 
# Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses. 

frutas = (
    "Laranja",
    "Pera",
    "Uva",
)
print(frutas)

letras = tuple("Python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) # A vírgula no final é uma boa prática para diferenciar a tupla de uma sentença comum
print(pais)
