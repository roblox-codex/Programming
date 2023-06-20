using System;

class FibonacciGenerator
{
    static void Main()
    {
        Console.Write("Enter the number of Fibonacci numbers to generate: ");
        int count = int.Parse(Console.ReadLine());

        Console.WriteLine("Fibonacci Sequence:");
        for (int i = 0; i < count; i++)
        {
            Console.Write(Fibonacci(i) + " ");
        }
    }

    static int Fibonacci(int n)
    {
        if (n <= 1)
            return n;

        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
}
