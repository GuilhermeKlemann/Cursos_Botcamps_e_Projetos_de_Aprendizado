using System;

namespace CursoCSharp.Colecoes {
    class Igualdade {
        public static void Executar() {
            var p1 = new Produto("Caneta", 1.89);
            var p2 = new Produto("Caneta", 1.89);
            var p3 = p2;

            Console.WriteLine(p1 == p2);
            Console.WriteLine(p2 == p3);

            //    Console.WriteLine(p1.Equals(p2));

            //            public override bool Equals(object obj) {
            //    Produto outroProduto = (Produto)obj;
            //    bool mesmoNome = Nome == outroProduto.Nome;
            //    bool mesmoPreco = Preco == outroProduto.Preco;
            //    return mesmoNome && mesmoPreco;

            //}
            //public override int GetHashCode() {
            //    return Nome.Length;
        }
    }

}

