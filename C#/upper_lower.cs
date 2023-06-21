using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a string: ");
        string input = Console.ReadLine();

        string toggledString = ToggleCase(input);
        Console.WriteLine("Toggled string: " + toggledString);
    }

    static string ToggleCase(string input)
    {
        char[] characters = input.ToCharArray();

        for (int i = 0; i < characters.Length; i++)
        {
            if (Char.IsLower(characters[i]))
            {
                characters[i] = Char.ToUpper(characters[i]);
            }
            else if (Char.IsUpper(characters[i]))
            {
                characters[i] = Char.ToLower(characters[i]);
            }
        }

        return new string(characters);
    }
}
