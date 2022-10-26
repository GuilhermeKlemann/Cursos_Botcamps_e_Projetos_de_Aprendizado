saldo = 1000
saque = 200
limite = 100

# Operador E / AND #
print(saldo >= saque and saque <= limite) # No AND todas as condições precisam ser verdadeiras para retornar True #

# Operador OU / OR #
print(saldo >= saque or saque <= limite) # No OR se apenas uma condição for verdadeira, retornará True #

# Operador Negação / NOT # 
contatos_emergencia = []

print(not 1000 > 1500) # No NOT todas as condições precisam ser falsas para retornar True #
print(not contatos_emergencia) 
print(not "Saque 1500;")
print(not "")

# Parênteses # 
saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)) # Os parênteses podem ser utilizados para definir#