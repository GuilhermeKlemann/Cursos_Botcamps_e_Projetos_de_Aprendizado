using System;

namespace CursoCSharp.Fundamentos {
    class OperadoresAritmeticos 
    {
        public static void Executar() {
            // Preço com Desconto
            var preco = 1000.00;
            var imposto = 355;
            var desconto = 0.1;

            double total = preco + imposto;
            var totalComDesconto = total - (total * desconto);
            Console.WriteLine("O preço final é {0}", totalComDesconto);


            // IMC 
            double peso = 74.5;
            double altura = 1.75;
            double imc = peso / Math.Pow(altura, 2);
            Console.WriteLine($"IMC é {imc}.");

            // Número Par/Ímpar
            int par = 24;
            int impar = 55;
            Console.WriteLine("{0}/2 tem o resto {1}", par, par % 2);
            Console.WriteLine("{0}/2 tem o resto {1}", impar, impar % 2);


        }
    }
}
