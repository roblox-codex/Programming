import java.util.Map;
import java.io.*;
import java.util.Scanner;
import java.util.Hashtable;
import java.util.*;

class HM
  {
    public static void main(String[] args)
    {
       
      final Map<Integer, String> ht1=new Hashtable<Integer, String>(100);

      final Map<Integer, String>ht2=new Hashtable<Integer, 
			String>(100);

       //Table 1
       //To insert values put statement is used
        ht1.put(11, "Sam");
        ht1.put(12, "Sid");
        ht1.put(13,"Samule");
        ht1.put(14,"Sate");

  
    System.out.println("\n\n===============================================================\n");
			
			//Table 2
      ht2.put(18,"O+ve");
      ht2.put(20,"B+ve");
      ht2.put(29,"A+ve");
      ht2.put(49,"AB+ve");
     
 System.out.println("Name and Enrollment of Students are: " +"\n" +ht1+"\n\n");

       System.out.println( "\n Blood Group and Age of Students are: " +"\n" +ht2+"\n\n");
     int delete;
     int delete2;

			
      System.out.println("Enter the element to be deleted from table 1");
      Scanner sc=new Scanner(System.in);
      delete=sc.nextInt();
      ht1.remove(delete);

      
      System.out.println("Enter the element to be deleted from table 2");
      delete2=sc.nextInt();
      ht2.remove(delete2);

      System.out.println("\nUpdated / Final map : "+"\n" +ht1+ "\n " +ht2+"\n\n");
        System.out.println("\n===============================================================\n");
    }
  }
