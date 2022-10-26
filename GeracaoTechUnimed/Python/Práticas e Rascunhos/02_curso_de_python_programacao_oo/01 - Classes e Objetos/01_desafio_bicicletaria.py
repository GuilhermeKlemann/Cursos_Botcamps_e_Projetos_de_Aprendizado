class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): 
        self.cor = cor 
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Bibiiiiiiiii!!")

    def parar(self):
        print("Freando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Acelerando a bicicleta...")
        print("Vruuuuuum!!")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")

        def _trocar_marchar():
            if nro_marcha > self.marcha:
                print("Marcha trocada!")
            else:
                print("Não foi possível trocar de marcha.")

    def __str__(self): 
        # return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bicicleta_1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
bicicleta_1.buzinar()
bicicleta_1.correr()
bicicleta_1.parar()
print(bicicleta_1.cor, bicicleta_1.modelo, bicicleta_1.ano, bicicleta_1.valor)

bicicleta_2 = Bicicleta("Verde", "Monark", 2000, 189)
print(bicicleta_2)
bicicleta_2.correr()


# __init__ é um método especial, invocado quando um objeto é instanciado. 
# O self é usado em classes no Python para indicar que você está referenciando alguma coisa do próprio objeto (sejam eles atributos ou métodos) - na verdade, o self é o próprio objeto em si.
# __str__ é um método especial, como __init__, usado para retornar uma representação de string de um objeto
# __class__ armazena uma referência à classe daquele objeto. Isto é, quando você possui uma instância de uma classe você consegue acessar qual é a classe que foi instanciada.
# __name__ é uma variável especial em Python. Ela obtém seu valor, dependendo de como executamos o script que a contém. Às vezes, você escreve um script com funções que também podem ser úteis para outros scripts. Em Python, você pode importar esse script como um módulo em outro script. Graças a essa variável especial, você pode decidir se quer executar o script ou se quer importar as funções definidas no script.
# __dict__  é um atributo e é a forma implementada, oficialmente, na linguagem Python de guardar atributos de instância nos objetos.