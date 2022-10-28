using System;
using System.Linq;

namespace CursoCSharp.TopicosAvancados
{
    class LINQ2
    {
        public static void Executar() {
            var alunos = new List<Aluno> {
                new Aluno { Nome = "Guilherme", Idade = 24, Nota = 8.5 },
                new Aluno { Nome = "Maria", Idade = 25, Nota = 9.0 },
                new Aluno { Nome = "Guilhotina", Idade = 26, Nota = 10.0 },
                new Aluno { Nome = "Ana", Idade = 21, Nota = 7.7 },
                new Aluno { Nome = "Jorge", Idade = 20, Nota = 4.3 },
                new Aluno { Nome = "Ana", Idade = 21, Nota = 7.5 },
                new Aluno { Nome = "Marcio", Idade = 19, Nota = 6.8 },
            };

            var guilhotina = alunos.Single(aluno => aluno.Nome.Equals("Guilhotina"));
            Console.WriteLine($"{guilhotina.Nome} {guilhotina.Nota}");

            var fulana = alunos.SingleOrDefault(aluno => aluno.Nome.Equals("Fulana"));
            if (fulana == null) {
                Console.WriteLine("Aluna Inexistente!");
            }

            var ana = alunos.First(aluno => aluno.Nome.Equals("Ana"));
            Console.WriteLine(ana.Nota);

            var sicrana = alunos.FirstOrDefault(aluno => aluno.Nota.Equals("Sicrana"));
            if (sicrana == null) {
                Console.WriteLine("Aluna Inexistente!");
            }

            var outraAna = alunos.LastOrDefault(aluno => aluno.Nome.Equals("Ana"));
            Console.WriteLine(outraAna.Nota);

            var exemploSkip = alunos.Skip(1).Take(3);
            foreach (var item in exemploSkip) {
                Console.WriteLine(item.Nome);
            }

            var maiorNota = alunos.Max(aluno => aluno.Nota);
            Console.WriteLine(maiorNota);

            var menorNota = alunos.Min(aluno => aluno.Nota);
            Console.WriteLine(menorNota);

            var somatorioNotas = alunos.Sum(aluno => aluno.Nota);
            Console.WriteLine(somatorioNotas);

            var mediaDaTurma = alunos.Average(aluno => aluno.Nota);
            Console.WriteLine(mediaDaTurma);

            var mediaDosAprovados = alunos.Where(aluno => aluno.Nota >= 7).Average(aluno => aluno.Nota);
            Console.WriteLine(mediaDosAprovados);
        }
    }
}
