using CursoCSharp.ClassesEMetodos;
using CursoCSharp.Fundamentos;
using System;
using System.Collections.Generic;

namespace CursoCSharp.Colecoes {
    public class Produtos {
        public string Nome;
        public double Preco;

        public Produtos(string nome, double preco) {
            Nome = nome;
            Preco = preco;
        }
    }

    class ColecoesSet {
        public static void Executar() {
            var livro = new Produto("Game of Thrones", 49.9);

            var carrinho = new HashSet<Produto>();
            carrinho.Add(livro);

            var combo = new HashSet<Produto> {
                new Produto("Camisa", 29.9),
                new Produto("8ª Temporada Game of Thrones", 99.9),
                new Produto("8ª Temporada Game of Thrones", 99.9),
                new Produto("Pôster", 10),
                new Produto("Pôster", 10)
            };

            carrinho.UnionWith(combo);
            Console.WriteLine(carrinho.Count);
            // carrinho.RemoveAt(3);

            foreach (var item in carrinho) {
            // Console.Write(carrinho.IndexOf(item));
                Console.WriteLine($" {item.Nome} {item.Preco}");
            }

            Console.WriteLine(carrinho.Count);
            carrinho.Add(livro);
            Console.WriteLine(carrinho.Count);
            // Console.WriteLine(carrinho.LastIndexOf(livro));


        }

        

    }

}



