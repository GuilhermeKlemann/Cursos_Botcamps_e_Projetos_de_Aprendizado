using System;

namespace CursoCSharp.ClassesEMetodos {
    class Membros {
        public static void Executar() {
            Pessoa fulano = new Pessoa();
            fulano.Nome = "Maria";
            fulano.Idade = 25;


            // Console.WriteLine($"{fulano.Nome} tem {fulano.Idade} anos.");

            fulano.ApresentarNoConsole();
            fulano.Zerar();
            fulano.ApresentarNoConsole();

            var beltrano = new Pessoa();
            beltrano.Nome = "Guilhotina";
            beltrano.Idade = 24;

            var apresentacaoDoBeltrano = beltrano.Apresentar();
            Console.WriteLine(apresentacaoDoBeltrano.Length);
            Console.WriteLine(apresentacaoDoBeltrano);
        }
    }
}
