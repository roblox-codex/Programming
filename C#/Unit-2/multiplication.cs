using System;

public class Multiplier
{
    private int num1;
    private int num2;

    public Multiplier(int number1, int number2)
    {
        num1 = number1;
        num2 = number2;
    }

    public int Multiply()
    {
        return num1 * num2;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Enter two numbers to multiply:");

        int num1 = Convert.ToInt32(Console.ReadLine());
        int num2 = Convert.ToInt32(Console.ReadLine());

        Multiplier multiplier = new Multiplier(num1, num2);

        int result = multiplier.Multiply();

        Console.WriteLine("Result: " + result);
    }
}
