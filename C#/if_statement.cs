using System.Collections.Generic;
using System;

namespace Condition
{
	class If_Statement
	{
		public static void Main(string[] args)
		{
			int number = 10;
			if (number < 6)
			{
				Console.WriteLine("{0} is less than 6", number);
			}

			Console.WriteLine("This statement is always executed.");
		}
	}
}
