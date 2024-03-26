import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number up to: ");
        int number = scanner.nextInt();

        int previousNumber = 0;
        int nextNumber = 1;

        System.out.print("Fibonacci Series up to " + number + " numbers : ");

        for (int i = 1; i <= number; ++i) {
            System.out.print(previousNumber + " ");
            int sum = previousNumber + nextNumber;
            previousNumber = nextNumber;
            nextNumber = sum;
        }
    }
}
