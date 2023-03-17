using System;

class Program
{
    static void Main(string[] args)
    {
        char startChar = 'A';
        int patternSize = 5;

        for (int i = 1; i <= patternSize; i++)
        {
            for (int j = 0; j < i; j++)
            {
                Console.Write(startChar + " ");
                startChar++;
            }
            Console.WriteLine();
        }
    }
}
