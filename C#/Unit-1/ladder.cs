using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Choose an option:");
        Console.WriteLine("1. If-Else Ladder");
        Console.WriteLine("2. Switch Statement");
        Console.Write("Enter your choice: ");
        int choice = int.Parse(Console.ReadLine());

        switch (choice)
        {
            case 1:
                IfElseLadder();
                break;
            case 2:
                SwitchStatement();
                break;
            default:
                Console.WriteLine("Invalid choice!");
                break;
        }
    }

    static void IfElseLadder()
    {
        Console.Write("Enter a number: ");
        int number = int.Parse(Console.ReadLine());

        if (number > 0)
        {
            Console.WriteLine("The number is positive.");
        }
        else if (number < 0)
        {
            Console.WriteLine("The number is negative.");
        }
        else
        {
            Console.WriteLine("The number is zero.");
        }
    }

    static void SwitchStatement()
    {
        Console.Write("Enter a day number (1-7): ");
        int dayNumber = int.Parse(Console.ReadLine());

        string dayName;

        switch (dayNumber)
        {
            case 1:
                dayName = "Monday";
                break;
            case 2:
                dayName = "Tuesday";
                break;
            case 3:
                dayName = "Wednesday";
                break;
            case 4:
                dayName = "Thursday";
                break;
            case 5:
                dayName = "Friday";
                break;
            case 6:
                dayName = "Saturday";
                break;
            case 7:
                dayName = "Sunday";
                break;
            default:
                dayName = "Invalid day";
                break;
        }

        Console.WriteLine("The day is: " + dayName);
    }
}
