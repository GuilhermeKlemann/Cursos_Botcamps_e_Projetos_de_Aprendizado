using System;

namespace CursoCSharp.ClassesEMetodos {
    class DesafioAtributo {

        int a = 10;
        public static void Executar() {
            // Acessar variável 'a' dentro do Método Executar!
            // Console.WriteLine(a);

            DesafioAtributo desafio = new DesafioAtributo();
            Console.WriteLine(desafio.a);
        }
    }
}
