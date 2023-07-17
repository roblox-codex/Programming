using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Temperature Converter");
        Console.WriteLine("1. Fahrenheit to Celsius");
        Console.WriteLine("2. Celsius to Fahrenheit");
        Console.Write("Enter Choice: ");
        int choice = Convert.ToInt32(Console.ReadLine());

        switch (choice)
        {
            case 1:
                FahrenheitToCelsius();
                break;
            case 2:
                CelsiusToFahrenheit();
                break;
            default:
                Console.WriteLine("Invalid choice. Please try again.");
                break;
        }
    }

    static void FahrenheitToCelsius()
    {
        Console.Write("Enter temperature in Fahrenheit: ");
        double fahrenheit = Convert.ToDouble(Console.ReadLine());

        double celsius = (fahrenheit - 32) * 5 / 9;

        Console.WriteLine("Temperature in Celsius: " + celsius.ToString("F2"));
    }

    static void CelsiusToFahrenheit()
    {
        Console.Write("Enter temperature in Celsius: ");
        double celsius = Convert.ToDouble(Console.ReadLine());

        double fahrenheit = (celsius * 9 / 5) + 32;

        Console.WriteLine("Temperature in Fahrenheit: " + fahrenheit.ToString("F2"));
    }
}
