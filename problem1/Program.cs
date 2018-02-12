using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem1
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = 0;
            for (int i = 0; i <= 1000; i++)
            {
                int remain3 = i % 3;
                int remain5 = i % 5;
                if (remain3 == 0 || remain5 == 0)
                {
                    Console.Write(i + ", ");
                    number = i + number;
                }
            }
            Console.WriteLine(number);
            Console.ReadLine();
        }
    }
}
