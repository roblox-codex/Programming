using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
 
 
namespace First_Ten_No
{
 
	  	class Program
	  	{
 
    	       	static void Main(string[] args)
    	       	{
 
       	              	 int s = 0;
 
        	             	for (int i = 1; i <= 10; i++)
        	             	{
 
           		               	Console.WriteLine(i);
            	                  	          s = s + i;
 
        	             	}
      	
        	                      	Console.WriteLine("Sum of Numbers = {0}", s);
    	       	}
 
	  	}
 }
