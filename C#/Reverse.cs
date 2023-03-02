using System.Collections.Generic;
using System;
using System.Linq;

namespace Reverse
{
    class Number
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a string to reverse: ");
            string input = Console.ReadLine();
            string output = Reverse(input);
            Console.WriteLine("Reversed string: " + output);
        }

        static string Reverse(string input)
        {
            char[] inputArray = input.ToCharArray();
            Array.Reverse(inputArray);
            return new string(inputArray);
        }
    }
}
