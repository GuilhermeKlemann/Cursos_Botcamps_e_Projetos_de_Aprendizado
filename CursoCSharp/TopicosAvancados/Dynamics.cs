using System;

namespace CursoCSharp.TopicosAvancados
{
    class Dynamics
    {
        public static void Executar() {
            dynamic meuObjeto = "teste";
            meuObjeto = 3;

            meuObjeto++;
            Console.WriteLine(meuObjeto);

            dynamic aluno = new System.Dynamic.ExpandoObject();
            aluno.nome = "Maria Guilhotina";
            aluno.nota = 9.9;
            aluno.idade = 25;

            Console.WriteLine($"{aluno.nome} {aluno.nota} {aluno.idade}");
        }
    }
}
