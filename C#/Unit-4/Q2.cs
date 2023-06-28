using System;
using System.Data;
using System.Data.SqlClient;

namespace ADO.NETUnboundModeExample
{
    class Program
    {
        static void Main(string[] args)
        {
            string connectionString = "YourConnectionString";
            string tableName = "YourTableName";

            // Create a new SqlConnection object
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();

                // Perform operations
                AddRecord(connection, tableName);
                SearchRecord(connection, tableName);
                EditRecord(connection, tableName);
                DeleteRecord(connection, tableName);

                connection.Close();
            }

            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        static void AddRecord(SqlConnection connection, string tableName)
        {
            // Prompt user for input
            Console.WriteLine("Enter data to add:");
            Console.Write("Name: ");
            string name = Console.ReadLine();
            Console.Write("Age: ");
            int age = int.Parse(Console.ReadLine());

            // Create a new SqlCommand object
            using (SqlCommand command = connection.CreateCommand())
            {
                command.CommandText = $"INSERT INTO {tableName} (Name, Age) VALUES (@Name, @Age)";
                command.Parameters.AddWithValue("@Name", name);
                command.Parameters.AddWithValue("@Age", age);

                // Execute the command
                int rowsAffected = command.ExecuteNonQuery();

                Console.WriteLine($"{rowsAffected} record(s) added.");
            }
        }

        static void SearchRecord(SqlConnection connection, string tableName)
        {
            // Prompt user for input
            Console.WriteLine("Enter name to search:");
            string searchName = Console.ReadLine();

            // Create a new SqlCommand object
            using (SqlCommand command = connection.CreateCommand())
            {
                command.CommandText = $"SELECT * FROM {tableName} WHERE Name = @SearchName";
                command.Parameters.AddWithValue("@SearchName", searchName);

                // Execute the command and retrieve the data
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    Console.WriteLine("Search Results:");
                    while (reader.Read())
                    {
                        Console.WriteLine($"ID: {reader["ID"]}, Name: {reader["Name"]}, Age: {reader["Age"]}");
                    }
                }
            }
        }

        static void EditRecord(SqlConnection connection, string tableName)
        {
            // Prompt user for input
            Console.WriteLine("Enter ID of the record to edit:");
            int id = int.Parse(Console.ReadLine());

            // Check if the record exists
            if (!RecordExists(connection, tableName, id))
            {
                Console.WriteLine("Record not found.");
                return;
            }

            // Prompt user for updated data
            Console.WriteLine("Enter updated data:");
            Console.Write("Name: ");
            string name = Console.ReadLine();
            Console.Write("Age: ");
            int age = int.Parse(Console.ReadLine());

            // Create a new SqlCommand object
            using (SqlCommand command = connection.CreateCommand())
            {
                command.CommandText = $"UPDATE {tableName} SET Name = @Name, Age = @Age WHERE ID = @ID";
                command.Parameters.AddWithValue("@Name", name);
                command.Parameters.AddWithValue("@Age", age);
                command.Parameters.AddWithValue("@ID", id);

                // Execute the command
                int rowsAffected = command.ExecuteNonQuery();

                Console.WriteLine($"{rowsAffected} record(s) updated.");
            }
        }

        static void DeleteRecord(SqlConnection connection, string tableName)
        {
            // Prompt user for input
            Console.WriteLine("Enter ID of the record to delete:");
            int id = int.Parse(Console.ReadLine());

            // Check if the record exists
            if (!RecordExists(connection, tableName, id))
            {
                Console.WriteLine("Record not found.");
                return;
            }

            // Create a new SqlCommand object
            using (SqlCommand command = connection.CreateCommand())
            {
                command.CommandText = $"DELETE FROM {tableName} WHERE ID = @ID";
                command.Parameters.AddWithValue("@ID", id);

                // Execute the command
                int rowsAffected = command.ExecuteNonQuery();

                Console.WriteLine($"{rowsAffected} record(s) deleted.");
            }
        }

        static bool RecordExists(SqlConnection connection, string tableName, int id)
        {
            // Create a new SqlCommand object
            using (SqlCommand command = connection.CreateCommand())
            {
                command.CommandText = $"SELECT COUNT(*) FROM {tableName} WHERE ID = @ID";
                command.Parameters.AddWithValue("@ID", id);

                // Execute the command and retrieve the count
                int count = (int)command.ExecuteScalar();

                return count > 0;
            }
        }
    }
}
