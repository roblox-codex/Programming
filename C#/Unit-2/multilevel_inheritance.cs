using System;

public class Animal
{
    public void Eat()
    {
        Console.WriteLine("Animal is eating.");
    }
}

public class Mammal : Animal
{
    public void Run()
    {
        Console.WriteLine("Mammal is running.");
    }
}

public class Dog : Mammal
{
    public void Bark()
    {
        Console.WriteLine("Dog is barking.");
    }
}

public class Program
{
    public static void Main()
    {
        Dog dog = new Dog();
        dog.Eat();
        dog.Run();
        dog.Bark();
    }
}
