using System;

class Program
{
    static void Main()
    {
        try
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            int result = 10 / num;

            Console.WriteLine("Result: " + result);
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine("DivideByZeroException caught!");
            Console.WriteLine("Exception message: " + ex.Message);
        }
        catch (FormatException ex)
        {
            Console.WriteLine("Exception caught!");
            Console.WriteLine("Exception message: " + ex.Message);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception caught!");
            Console.WriteLine("Exception type: " + ex.GetType());
            Console.WriteLine("Exception message: " + ex.Message);
        }
        finally
        {
            Console.WriteLine("The program execution is complete.");
        }
    }
}
