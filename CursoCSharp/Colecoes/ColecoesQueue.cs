using System;
using System.Collections;
using System.Collections.Generic;

namespace CursoCSharp.Colecoes {
    class ColecoesQueue {
        public static void Executar() {
            var fila = new Queue<string>();

            fila.Enqueue("Fulano");
            fila.Enqueue("Sicrano");
            fila.Enqueue("Beltrano");

            Console.WriteLine(fila.Peek()); // Retorna o primeiro item (fulano) da fila, não removendo ele da fila.
            Console.WriteLine(fila.Count); // Conta quantos itens estão na fila.

            Console.WriteLine(fila.Dequeue()); // Retorna o primeiro item (fulano) da fila, removendo ele da fila.
            Console.WriteLine(fila.Count);

            foreach (var pessoa in fila) { // Retorna os itens restantes da fila.
                Console.WriteLine(pessoa);
            }

            var salada = new Queue();
            salada.Enqueue(3);
            salada.Enqueue("Item");
            salada.Enqueue(true);
            salada.Enqueue(3.14);

            Console.WriteLine(salada.Contains("Item"));
        }
    }
}
