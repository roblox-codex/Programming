using System;
using System.Data;
using System.Data.SqlClient;

class Program
{
    static void Main()
    {
        // Connection string
        string connectionString = "Data Source=(local);Initial Catalog=YourDatabase;Integrated Security=True";

        // Create connection object
        SqlConnection connection = new SqlConnection(connectionString);

        try
        {
            // Open the connection
            connection.Open();
            Console.WriteLine("Connection opened successfully.");

            // Perform database operations
            // ...

            // Close the connection
            connection.Close();
            Console.WriteLine("Connection closed successfully.");
        }
        catch (SqlException ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
        finally
        {
            // Ensure the connection is closed
            if (connection.State != ConnectionState.Closed)
                connection.Close();
        }

        Console.ReadLine();
    }
}
