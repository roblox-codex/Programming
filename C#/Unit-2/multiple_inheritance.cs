using System;

public interface IPerson
{
    void Introduction();
}

public interface IStudent
{
    void Study();
}

public class Student : IStudent, IPerson
{
    public string Name { get; set; }

    public Student(string name)
    {
        Name = name;
    }

    public void Study()
    {
        Console.WriteLine($"{Name} is studying.");
    }

    public void Introduction()
    {
        Console.WriteLine($"Hi, my name is {Name}.");
    }
}

public class Program
{
    public static void Main()
    {
        Console.Write("Enter student's name: ");
        string name = Console.ReadLine();

        Student student = new Student(name);
        student.Introduction();
        student.Study();
    }
}
