using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the number of Fibonacci numbers to generate: ");
        int n = int.Parse(Console.ReadLine());

        Console.WriteLine("Fibonacci series:");
        for (int i = 0; i < n; i++)
        {
            int fib = Fibonacci(i);
            Console.Write(fib + " ");
        }
    }

    static int Fibonacci(int n)
    {
        if (n <= 1)
            return n;

        int a = 0;
        int b = 1;
        int fib = 0;

        for (int i = 2; i <= n; i++)
        {
            fib = a + b;
            a = b;
            b = fib;
        }

        return fib;
    }
}
