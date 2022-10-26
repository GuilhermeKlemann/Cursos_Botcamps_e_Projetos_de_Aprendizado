using System;

namespace CursoCSharp.Fundamentos {
    class OperadoresLogicos {
        static public void Executar() {
            var executouTrabalho1 = true;
            var executouTrabalho2 = false;

            bool comprouTV50 = executouTrabalho1 && executouTrabalho2;
            Console.WriteLine("Comprou a TV 50? {0}", comprouTV50);

            // Operadores Binários
            var comprouSorvete = executouTrabalho1 || executouTrabalho2;
            Console.WriteLine("Comprou o sorvete? {0}", comprouSorvete);

            var comprouTV32 = executouTrabalho1 ^ executouTrabalho2;
            Console.WriteLine("Comprou a TV 32? {0}", comprouTV32);

            // Operadores Unários
            Console.WriteLine("Mais saudável? {0}", !comprouSorvete);
        }
    }
}
