using System;

namespace CursoCSharp.ClassesEMetodos {

    public class Cliente1 {
        public string Nome;
        readonly DateTime Nascimento;

        public Cliente1(string nome, DateTime nascimento) {
            Nome = nome;
            Nascimento  = nascimento;
        }

        public string GetDataDeNascimento() {
            return String.Format("{0}/{1}/{2}", Nascimento.Day, Nascimento.Month, Nascimento.Year);
        }
    }
    class Reandonly {
        public static void Executar() {
            var novoCliente = new Cliente1("Maria Guilhotina", new DateTime(1997, 11, 1));

            Console.WriteLine(novoCliente.Nome);
            Console.WriteLine(novoCliente.GetDataDeNascimento());
        }
    }
}
