using System;

namespace CursoCSharp.Fundamentos {
    class Inferencia {
        public static void Executar() {
            var nome = "Guilherme";
            // nome = 123 (Não é possível converter implicitamente tipo "int" em "string")
            Console.WriteLine(nome);


            var idade = 24;
            // (ou) int idade;
            Console.WriteLine(idade);

            int a;
            a = 3; // É possível declarar uma variável e definir seu valor em diferentes linhas...

            int b = 2; // ...Ou simplesmente declarar a variável ao mesmo tempo em que define seu valor.

            Console.WriteLine(a + b);
        }
    }
}
