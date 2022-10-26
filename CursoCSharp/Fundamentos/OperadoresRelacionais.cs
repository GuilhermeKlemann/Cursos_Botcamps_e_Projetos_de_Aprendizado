using System;

namespace CursoCSharp.Fundamentos {
    class OperadoresRelacionais 
    {
        public static void Executar() {
            // double nota = 6.0;
            Console.Write("Digite a nota: ");
            double.TryParse(Console.ReadLine(), out double nota);
            double notaDeCorte = 7.0;

            Console.WriteLine("Nota Inválida? {0}", nota > 10.0); // > maior que
            Console.WriteLine("Nota Inválida? {0}", nota < 0.0);
            Console.WriteLine("Perfeito? {0}", nota == 10.0); // == igual
            Console.WriteLine("Tem como melhorar? {0}", nota != 10.0); // != diferente
            Console.WriteLine("Passou por média? {0}", nota >= notaDeCorte); // >= maior ou igual
            Console.WriteLine("Recuperação? {0}", nota < notaDeCorte); // < menor que
            Console.WriteLine("Reprovado? {0}", nota <= 3.0); // <= menor ou igual

        }
    }
}
