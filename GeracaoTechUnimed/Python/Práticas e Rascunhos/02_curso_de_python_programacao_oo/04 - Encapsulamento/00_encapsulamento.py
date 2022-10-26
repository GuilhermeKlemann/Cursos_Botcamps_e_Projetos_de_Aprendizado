# O encapsulamento é um dos conceitos fundamentais em programação orientada a objetos. 
# Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. 
# Isso impõe restrições ao acesso direto a variáveis ​​e métodos e pode evitar a modificação acidental de dados. 
# Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

# Em linguagens como Java e C++, existem palavras reservadas para definir o nível de acesso aos atributos e métodos da classe. 
# Em Python não temos palavras reservadas, porém usamos convenções no nome do recurso ("_variável"), para definir se a variável é pública ou privada.
# Público: Pode ser acessado de fora da classe; # Privado: Só pode ser acessado pela classe.
# Todos os recursos são públicos, a menos que o nome inicie com underline. 
# O interpretador Python não irá garantir a proteção do recurso, mas por ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por underline, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar o método fora do escopo da classe.


# Properties - Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

