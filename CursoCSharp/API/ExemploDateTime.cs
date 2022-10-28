using System;
using System.IO;

namespace CursoCSharp.API
{
    class ExemploDateTime
    {
        public static void Executar() {
            var dateTime = new DateTime(day: 1, month: 11, year: 1997);

            Console.WriteLine(dateTime.Day);
            Console.WriteLine(dateTime.Month);
            Console.WriteLine(dateTime.Year);

            // Sem Horas
            var hoje = DateTime.Today;
            Console.WriteLine(hoje);

            // Com Horas
            var diaAtual = DateTime.Now;
            Console.WriteLine(diaAtual);
            Console.WriteLine("Hora: " + diaAtual.Hour);
            Console.WriteLine("Minutos: " + diaAtual.Minute);

            var amanha = diaAtual.AddDays(1);
            Console.WriteLine(amanha);

            var ontem = diaAtual.AddDays(-1);
            Console.WriteLine(ontem);

            Console.WriteLine(diaAtual.ToString("dd"));
            Console.WriteLine(diaAtual.ToString("d"));
            Console.WriteLine(diaAtual.ToString("D"));
            Console.WriteLine(diaAtual.ToString("g"));
            Console.WriteLine(diaAtual.ToString("G"));
            Console.WriteLine(diaAtual.ToString("dd-MM-yyyy HH:mm"));
        }
    }
}
