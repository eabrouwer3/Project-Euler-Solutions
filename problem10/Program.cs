using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem10
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = 0;
            for (int i = 2; i < 2000000; i++)
            {
                int r2 = i % 2;
                int r3 = i % 3;
                int r5 = i % 5;
                int r7 = i % 7;
                if (r2 == 0 || r3 == 0 || r5 == 0 || r7 == 0)
                {
                }
                else
                {
                    Console.Write(i + ", ");
                    number += i;
                }
            }
            Console.WriteLine("");
            Console.WriteLine(number);
            Console.ReadLine();
        }
    }
}
