using System;

class Program
{
    static void Main()
    {
        char choice;
        do
        {
            Console.WriteLine("Menu:");
            Console.WriteLine("a. Convert Binary to Decimal");
            Console.WriteLine("b. Convert Decimal to Binary");
            Console.WriteLine("c. Convert Hexadecimal to Octal");
            Console.WriteLine("d. Convert Octal to Decimal");
            Console.WriteLine("e. Exit");
            Console.Write("Enter your choice (a, b, c, d, or e): ");
            choice = char.ToLower(Console.ReadKey().KeyChar);
            Console.WriteLine();

            switch (choice)
            {
                case 'a':
                    ConvertBinaryToDecimal();
                    break;
                case 'b':
                    ConvertDecimalToBinary();
                    break;
                case 'c':
                    ConvertHexadecimalToOctal();
                    break;
                case 'd':
                    ConvertOctalToDecimal();
                    break;
                case 'e':
                    Console.WriteLine("Exiting the program...");
                    break;
                default:
                    Console.WriteLine("Invalid choice!");
                    break;
            }

            Console.WriteLine();
        } while (choice != 'e');
    }

    static void ConvertBinaryToDecimal()
    {
        Console.Write("Enter a binary number: ");
        string binary = Console.ReadLine();

        int decimalNumber = Convert.ToInt32(binary, 2);
        Console.WriteLine("Decimal equivalent: " + decimalNumber);
    }

    static void ConvertDecimalToBinary()
    {
        Console.Write("Enter a decimal number: ");
        int decimalNumber = int.Parse(Console.ReadLine());

        string binary = Convert.ToString(decimalNumber, 2);
        Console.WriteLine("Binary equivalent: " + binary);
    }

    static void ConvertHexadecimalToOctal()
    {
        Console.Write("Enter a hexadecimal number: ");
        string hexadecimal = Console.ReadLine();

        int decimalNumber = Convert.ToInt32(hexadecimal, 16);
        string octal = Convert.ToString(decimalNumber, 8);
        Console.WriteLine("Octal equivalent: " + octal);
    }

    static void ConvertOctalToDecimal()
    {
        Console.Write("Enter an octal number: ");
        string octal = Console.ReadLine();

        int decimalNumber = Convert.ToInt32(octal, 8);
        Console.WriteLine("Decimal equivalent: " + decimalNumber);
    }
}
