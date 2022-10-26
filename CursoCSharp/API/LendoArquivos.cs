﻿using System;
using System.IO;
using System.Xml;

namespace CursoCSharp.API
{
    class LendoArquivos
    {
        public static void Executar() {
            var path = @"~/lendo_arquivos.txt".ParseHome();

            if (File.Exists(path)) {
                using (StreamWriter sw = File.AppendText(path)) {
                    sw.WriteLine("Produto;Preco;Quantidade");
                    sw.WriteLine("Caneta Bic Preta;3.59;89");
                    sw.WriteLine("Borracha Branca; 2.89; 27");
                }
            }

            try {
                using (StreamReader sr = new StreamReader(path)) {
                    var texto = sr.ReadToEnd();
                    Console.WriteLine(texto);
                }
            } catch (Exception ex) {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
