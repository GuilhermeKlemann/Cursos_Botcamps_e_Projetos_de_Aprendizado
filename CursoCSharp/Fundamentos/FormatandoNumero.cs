using System;
using System.Globalization;

namespace CursoCSharp.Fundamentos {
    class FormatandoNumero {
        public static void Executar() {
            double valor = 15.175;
            Console.WriteLine(valor.ToString("F1")); // Uma casa após a vírgula
            Console.WriteLine(valor.ToString("C")); // Transforma em valor monetário
            Console.WriteLine(valor.ToString("P")); // Valor percentual * 100
            Console.WriteLine(valor.ToString("#.##")); // Transforma o número para duas casas após a vírgula

            CultureInfo cultura = new CultureInfo("en-US");
            Console.WriteLine(valor.ToString("C0", cultura));

            int inteiro = 256;
            Console.WriteLine(inteiro.ToString("D10"));

        }
    }
}
