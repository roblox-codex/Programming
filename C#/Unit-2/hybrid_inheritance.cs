using System;

// Base interface
interface IStudent
{
    string Name { get; set; }
    void DisplayStudent();
}

// First derived interface
interface IScienceStudent : IStudent
{
    void DisplayScienceStudent();
}

// Second derived interface
interface IArtsStudent : IStudent
{
    void DisplayArtsStudent();
}

// Derived class implementing both IScienceStudent and IArtsStudent
class HybridStudent : IScienceStudent, IArtsStudent
{
    public string Name { get; set; }

    public void DisplayStudent()
    {
        Console.WriteLine("Student Name: " + Name);
    }

    public void DisplayScienceStudent()
    {
        Console.WriteLine("Science Student: " + Name);
    }

    public void DisplayArtsStudent()
    {
        Console.WriteLine("Arts Student: " + Name);
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Creating object of the hybrid class
        HybridStudent hybridStudent = new HybridStudent();
        hybridStudent.Name = "Michael Johnson";

        // Calling methods from the hybrid class
        hybridStudent.DisplayStudent();         // Output: Student Name: Michael Johnson
        hybridStudent.DisplayScienceStudent();  // Output: Science Student: Michael Johnson
        hybridStudent.DisplayArtsStudent();     // Output: Arts Student: Michael Johnson
    }
}
