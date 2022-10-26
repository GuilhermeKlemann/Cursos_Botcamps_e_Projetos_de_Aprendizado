# Em Python tudo é objeto, dessa forma, funções também são objetos, o que as tornam objetos de primeira classe.
# Com isso, podemos atribuir funções e variáveis, passá-las como parâmetros para funções, usá-las como valores em estruturas de dados(listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função(closures).

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def test(a, b):
    return a*2 + b*3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)
exibir_resultado(10, 10, dividir)
exibir_resultado(10, 10, test)
