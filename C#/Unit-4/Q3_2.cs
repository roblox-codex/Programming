class Program
{
    static void Main(string[] args)
    {
        DatabaseManager dbManager = new DatabaseManager();

        // Display menu options to the user
        while (true)
        {
            Console.WriteLine("Customer Database Management");
            Console.WriteLine("1. View Customers");
            Console.WriteLine("2. Add Customer");
            Console.WriteLine("3. Update Customer");
            Console.WriteLine("4. Delete Customer");
            Console.WriteLine("5. Exit");
            Console.Write("Enter option: ");
            string option = Console.ReadLine();

            switch (option)
            {
                case "1":
                    // View Customers
                    DataTable customers = dbManager.GetCustomers();
                    foreach (DataRow row in customers.Rows)
                    {
                        Console.WriteLine($"Customer ID: {row["CustomerID"]}");
                        Console.WriteLine($"Name: {row["FirstName"]} {row["LastName"]}");
                        Console.WriteLine($"Email: {row["Email"]}");
                        Console.WriteLine($"Phone Number: {row["PhoneNumber"]}");
                        Console.WriteLine();
                    }
                    break;
                case "2":
                    // Add Customer
                    Customer newCustomer = GetCustomerDetails();
                    dbManager.AddCustomer(newCustomer);
                    Console.WriteLine("Customer added successfully.");
                    break;
                case "3":
                    // Update Customer
                    int customerID = GetCustomerID();
                    Customer updatedCustomer = GetCustomerDetails();
                    updatedCustomer.CustomerID = customerID;
                    dbManager.UpdateCustomer(updatedCustomer);
                    Console.WriteLine("Customer updated successfully.");
                    break;
                case "4":
                    // Delete Customer
                    int deleteCustomerID = GetCustomerID();
                    dbManager.DeleteCustomer(deleteCustomerID);
                    Console.WriteLine("Customer deleted successfully.");
                    break;
                case "5":
                    // Exit the application
                    return;
                default:
                    Console.WriteLine("Invalid option. Please try again.");
                    break;
            }
        }
    }

    static Customer GetCustomerDetails()
    {
        Console.Write("Enter First Name: ");
        string firstName = Console.ReadLine();
        Console.Write("Enter Last Name: ");
        string lastName = Console.ReadLine();
        Console.Write("Enter Email: ");
        string email = Console.ReadLine();
        Console.Write("Enter Phone Number: ");
        string phoneNumber = Console.ReadLine();

        return new Customer
        {
            FirstName = firstName,
            LastName = lastName,
            Email = email,
            PhoneNumber = phoneNumber
        };
    }

    static int GetCustomerID()
    {
        Console.Write("Enter Customer ID: ");
        string customerIDInput = Console.ReadLine();
        int customerID;
        if (int.TryParse(customerIDInput, out customerID))
        {
            return customerID;
        }
        else
        {
            Console.WriteLine("Invalid Customer ID. Please try again.");
            return GetCustomerID();
        }
    }
}
