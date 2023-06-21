using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();

        int vowelCount = CountVowels(input);

        Console.WriteLine($"Number of vowels: {vowelCount}");
    }

    static int CountVowels(string str)
    {
        int count = 0;

        foreach (char c in str)
        {
            if (IsVowel(c))
            {
                count++;
            }
        }

        return count;
    }

    static bool IsVowel(char c)
    {
        char lowerChar = char.ToLower(c);

        return lowerChar == 'a' || lowerChar == 'e' || lowerChar == 'i' || lowerChar == 'o' || lowerChar == 'u';
    }
}
