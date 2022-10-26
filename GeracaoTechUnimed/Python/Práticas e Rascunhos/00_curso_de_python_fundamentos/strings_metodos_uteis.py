# Letras maíusculas, minúscuas e títulos #

curso = "pYtHoN"

print(curso.upper())
print(curso.lower())
print(curso.title())


# Eliminando espaços em branco #

curso_2 = "    Python  "

print(curso_2.strip())
print(curso_2.lstrip())
print(curso_2.rstrip())

# Junções e Centralização #

curso_3 = "Python"

print(curso_3.center(10, "#")) # Completa a quantidade de caracteres com o caractere definido #
print(".".join(curso_3)) # Completa com o caractere definido item a item (letra a letra) da string#

