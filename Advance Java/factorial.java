import java.util.Scanner;
import java.math.BigInteger;

 public class Factorial{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = scanner.nextInt();

        BigInteger fact = BigInteger.ONE;
        for(int i=1; i<=num; i++){
            fact = fact.multiply(BigInteger.valueOf(i));
        }

        System.out.println("Factorial of " + num + " is " + fact);
    }
}
