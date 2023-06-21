using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the value for a: ");
        int a = int.Parse(Console.ReadLine());

        Console.Write("Enter the value for b: ");
        int b = int.Parse(Console.ReadLine());

        Console.WriteLine("Before swapping:");
        Console.WriteLine("a = " + a);
        Console.WriteLine("b = " + b);

        int temp = a;
        a = b;
        b = temp;

        Console.WriteLine("After swapping:");
        Console.WriteLine("a = " + a);
        Console.WriteLine("b = " + b);
    }
}
