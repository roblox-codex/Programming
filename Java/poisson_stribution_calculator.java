import java.util.Scanner;

public class PoissonCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Get user input for x and lambda
        System.out.print("Enter the value of x: ");
        int x = input.nextInt();
        System.out.print("Enter the value of lambda: ");
        double lambda = input.nextDouble();

        // Calculate the Poisson distribution
        double poisson = Math.pow(lambda, x) * Math.exp(-lambda) / factorial(x);

        // Display the result
        System.out.printf("P(X = %d) = %.4f", x, poisson);
    }

    // Method to calculate the factorial of a number
    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorial(n-1);
        }
    }
}
