using System;

public class Number
{
    public int Value { get; set; }

    public Number(int value)
    {
        Value = value;
    }

    // Overloading the '+' operator
    public static Number operator +(Number n1, Number n2)
    {
        int result = n1.Value + n2.Value;
        return new Number(result);
    }

    // Overloading the '-' operator
    public static Number operator -(Number n1, Number n2)
    {
        int result = n1.Value - n2.Value;
        return new Number(result);
    }

    // Overriding the ToString method for easy printing
    public override string ToString()
    {
        return Value.ToString();
    }
}

public class Program
{
    public static void Main()
    {
        Console.Write("Enter the first number: ");
        int number1 = int.Parse(Console.ReadLine());
        Number n1 = new Number(number1);

        Console.Write("Enter the second number: ");
        int number2 = int.Parse(Console.ReadLine());
        Number n2 = new Number(number2);

        Number sum = n1 + n2;
        Console.WriteLine($"Sum: {n1} + {n2} = {sum}");

        Number difference = n1 - n2;
        Console.WriteLine($"Difference: {n1} - {n2} = {difference}");
    }
}
