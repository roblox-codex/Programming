using System;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Outer try block
            int[] numbers = { 1, 2, 3, 4, 5 };
            int result = numbers[10]; // Accessing an invalid index
            Console.WriteLine("Result: " + result); // This line will not be executed
        }
        catch (IndexOutOfRangeException ex)
        {
            // Catching the specific exception in the outer catch block
            Console.WriteLine("Outer Catch Block - Index out of range");
            Console.WriteLine("Exception message: " + ex.Message);

            try
            {
                // Inner try block
                string str = null;
                int length = str.Length; // Null reference exception
                Console.WriteLine("Length: " + length); // This line will not be executed
            }
            catch (NullReferenceException ex2)
            {
                // Catching the specific exception in the inner catch block
                Console.WriteLine("Inner Catch Block - Null reference exception");
                Console.WriteLine("Exception message: " + ex2.Message);
            }
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
