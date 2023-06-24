using System;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Code that may throw an exception
            int a = 10;
            int b = 0;
            int result = a / b;
            Console.WriteLine("Result: " + result); // This line will not be executed
        }
        catch (DivideByZeroException ex)
        {
            // Catching the specific exception
            Console.WriteLine("Error: Divide by zero");
            Console.WriteLine("Exception message: " + ex.Message);
        }
        catch (Exception ex)
        {
            // Catching any other exception
            Console.WriteLine("An error occurred:");
            Console.WriteLine("Exception type: " + ex.GetType());
            Console.WriteLine("Exception message: " + ex.Message);
        }
        finally
        {
            // Code that will always execute, regardless of whether an exception occurred or not
            Console.WriteLine("The program execution is complete.");
        }
    }
}
