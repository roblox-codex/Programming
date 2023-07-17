using System;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // ArrayList: A non-generic collection that can store objects of any type.
        ArrayList arrayList = new ArrayList();
        arrayList.Add("Apple");
        arrayList.Add("Banana");
        arrayList.Add("Cherry");

        Console.WriteLine("ArrayList:");
        foreach (var item in arrayList)
        {
            Console.WriteLine(item);
        }

        // List<T>: A generic collection that stores elements of a specific type.
        List<string> list = new List<string>();
        list.Add("Dog");
        list.Add("Cat");
        list.Add("Elephant");

        Console.WriteLine("\nList<T>:");
        foreach (var item in list)
        {
            Console.WriteLine(item);
        }

        // Stack<T>: A generic collection that represents a last-in, first-out (LIFO) stack.
        Stack<string> stack = new Stack<string>();
        stack.Push("Red");
        stack.Push("Green");
        stack.Push("Blue");

        Console.WriteLine("\nStack<T>:");
        while (stack.Count > 0)
        {
            Console.WriteLine(stack.Pop());
        }

        // Queue<T>: A generic collection that represents a first-in, first-out (FIFO) queue.
        Queue<string> queue = new Queue<string>();
        queue.Enqueue("Monday");
        queue.Enqueue("Tuesday");
        queue.Enqueue("Wednesday");

        Console.WriteLine("\nQueue<T>:");
        while (queue.Count > 0)
        {
            Console.WriteLine(queue.Dequeue());
        }

        // Dictionary<TKey, TValue>: A generic collection that stores key/value pairs.
        Dictionary<string, int> dictionary = new Dictionary<string, int>();
        dictionary.Add("One", 1);
        dictionary.Add("Two", 2);
        dictionary.Add("Three", 3);

        Console.WriteLine("\nDictionary<TKey, TValue>:");
        foreach (var kvp in dictionary)
        {
            Console.WriteLine(kvp.Key + ": " + kvp.Value);
        }

        // HashSet<T>: A generic collection that stores unique elements.
        HashSet<string> hashSet = new HashSet<string>();
        hashSet.Add("Apple");
        hashSet.Add("Banana");
        hashSet.Add("Cherry");

        Console.WriteLine("\nHashSet<T>:");
        foreach (var item in hashSet)
        {
            Console.WriteLine(item);
        }
    }
}
