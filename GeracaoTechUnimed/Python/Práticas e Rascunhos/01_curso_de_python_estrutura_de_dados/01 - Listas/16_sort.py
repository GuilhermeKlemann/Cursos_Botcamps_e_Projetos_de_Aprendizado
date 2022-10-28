linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort() # Sorteando ordem alfabética
print(linguagens)

linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort(reverse=True) # Sorteando de trás pra frente
print(linguagens)

linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort(key=lambda x: len(x)) # Sorteando do menor para o maior número de caracteres
print(linguagens)

linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # Sorteando do maior para o menor número de caracteres
print(linguagens)