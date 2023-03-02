using System.Collections.Generic;
using System;
using System.Linq;

namespace factorial
{
    class Factorial
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number to find the factorial of:");
            int input = Convert.ToInt32(Console.ReadLine());
            int output = Fact(input);
            Console.WriteLine("Factorial: " + output);
        }

        static int Fact(int input)
        {
            int output = 1;
            for (int i = 1; i <= input; i++)
            {
                output *= i;
            }
            return output;
        }
    }
}
