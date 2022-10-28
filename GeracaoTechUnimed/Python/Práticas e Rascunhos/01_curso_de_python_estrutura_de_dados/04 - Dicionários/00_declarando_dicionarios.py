# Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. 
# Dicionários são delimitados por chaves:{}, e contém uma lista d epares chave:valor separadas por vírgulas.

pessoa = {"nome": "Guilherme", "idade": 24} 
print(pessoa)

pessoa = dict(nome="Guilherme", idade=24) # Usando o construtor dict
print(pessoa)

pessoa["telefone"] = "(47) 99756-6537"
print(pessoa)

pessoa["nome"] = "Maria"
print(pessoa)