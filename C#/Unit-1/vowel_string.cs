using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();

        string vowels = FindVowels(input);
        Console.WriteLine("Vowels in the string: " + vowels);
    }

    static string FindVowels(string input)
    {
        string vowels = "";

        foreach (char c in input)
        {
            if (IsVowel(c))
            {
                if (!vowels.Contains(c))
                {
                    vowels += c;
                }
            }
        }

        return vowels;
    }

    static bool IsVowel(char c)
    {
        char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
        return Array.IndexOf(vowels, char.ToLower(c)) != -1;
    }
}
