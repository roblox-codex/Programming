using System;

public class Adder
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Adder adder = new Adder();

        Console.WriteLine("Enter two integers:");
        int int1 = Convert.ToInt32(Console.ReadLine());
        int int2 = Convert.ToInt32(Console.ReadLine());
        int intResult = adder.Add(int1, int2);

        Console.WriteLine("Enter two doubles:");
        double double1 = Convert.ToDouble(Console.ReadLine());
        double double2 = Convert.ToDouble(Console.ReadLine());
        double doubleResult = adder.Add(double1, double2);

        Console.WriteLine("Result of integer addition: " + intResult);
        Console.WriteLine("Result of double addition: " + doubleResult);
    }
}
