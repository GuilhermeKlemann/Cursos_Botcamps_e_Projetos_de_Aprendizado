using System;

namespace CursoCSharp.OO
{
    sealed class SemFilho
    {
        public double ValorDaFortuna() {
            return 1_407_033.65;
        }
    }

    // class SouFilho : SemFilho { }

    class Avo
    {
        public virtual bool HonrarNomeFamilia() {
            return true;
        }
    }

    class Pai : Avo
    {
        public sealed override bool HonrarNomeFamilia() {
            return true;
        }
    }

    class FilhoRebelde : Pai
    {
        //public override boolHonrarNomeFamilia() {
        //    return false
        //}
    }
    class Sealed
    {
        static public void Executar() {
            SemFilho semFilho = new SemFilho();
            Console.WriteLine(semFilho.ValorDaFortuna());

            FilhoRebelde filho = new FilhoRebelde();
            Console.WriteLine(filho.HonrarNomeFamilia());
        }
    }
}
