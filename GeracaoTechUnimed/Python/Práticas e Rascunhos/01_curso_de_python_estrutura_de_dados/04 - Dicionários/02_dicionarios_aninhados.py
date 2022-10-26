# Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como strings e números.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "3344-9871"},
    "guilhotina@gmail.com": {"nome": "Guilhotina", "telefone": "3333-7766", "extra": {"a": 1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)

extra = contatos["guilhotina@gmail.com"]["extra"]
print(extra)
