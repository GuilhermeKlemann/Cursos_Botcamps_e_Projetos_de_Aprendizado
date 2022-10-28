using System;

namespace CursoCSharp.ClassesEMetodos {

    public enum Genero { Acao, Aventura, Terror, Animacao, Comedia, Drama };
    public class Filme {
        public string Titulo;
        public Genero GeneroDoFilme;
    }
    class ExemploEnum {
        public static void Executar() {
            int id = (int)Genero.Animacao;
            Console.WriteLine(id);

            var filmeParaFamilia = new Filme();
            filmeParaFamilia.Titulo = "Meu amigo Totoro";
            filmeParaFamilia.GeneroDoFilme = Genero.Animacao;

            Console.WriteLine("{0} é {1}!", filmeParaFamilia.Titulo, filmeParaFamilia.GeneroDoFilme);
        }
    }
}
