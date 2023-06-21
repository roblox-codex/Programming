using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();

        bool isPalindrome = CheckPalindrome(input);

        if (isPalindrome)
        {
            Console.WriteLine("The string is a palindrome.");
        }
        else
        {
            Console.WriteLine("The string is not a palindrome.");
        }
    }

    static bool CheckPalindrome(string str)
    {
        int left = 0;
        int right = str.Length - 1;

        while (left < right)
        {
            if (str[left] != str[right])
            {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
