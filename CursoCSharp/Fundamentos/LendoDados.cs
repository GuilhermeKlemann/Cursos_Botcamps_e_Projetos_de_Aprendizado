using System;
using System.Globalization; // Está sendo utilizado para rodar o CultureInfo.InvariantCulture (e a partir disso permitir que o . ou , sejam indiferentes ao serem inseridos no terminal.

namespace CursoCSharp.Fundamentos {
    class LendoDados {
        public static void Executar() {
            Console.WriteLine("Qual é o seu nome? ");
            string nome = Console.ReadLine();

            Console.Write("Qual é a sua idade? ");
            int idade = int.Parse(Console.ReadLine());

            Console.WriteLine("Qual é o seu salário? ");
            double salario = double.Parse(Console.ReadLine(),
                CultureInfo.InvariantCulture);

            Console.WriteLine($"{nome} {idade} R${salario}");
        }
    }
}
