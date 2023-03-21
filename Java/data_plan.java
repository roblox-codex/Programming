import java.util.Scanner;

public class Service {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Display the available plans to the user
        System.out.println("AirWaves service plans:");
        System.out.println("A - Talk (<500 min), Text (none), Data (none) - $49/month");
        System.out.println("B - Talk (<500 min), Text (any), Data (none) - $55/month");
        System.out.println("C - Talk (>=500 min), Text (<100), Data (none) - $61/month");
        System.out.println("D - Talk (>=500 min), Text (>=100), Data (none) - $70/month");
        System.out.println("E - Talk (any), Text (any), Data (<3 GB) - $79/month");
        System.out.println("F - Talk (any), Text (any), Data (>=3 GB) - $87/month");

        // Prompt the user for their maximum talk minutes, text messages, and data usage
        System.out.print("Enter the maximum number of talk minutes per month: ");
        int talkMinutes = scanner.nextInt();
        System.out.print("Enter the maximum number of text messages per month: ");
        int textMessages = scanner.nextInt();
        System.out.print("Enter the maximum amount of data per month (in GB): ");
        int dataUsage = scanner.nextInt();

        // Determine the best plan for the user based on their inputs
        String recommendedPlan = "";
        int recommendedPrice = Integer.MAX_VALUE;
        if (talkMinutes < 500 && textMessages == 0 && dataUsage == 0) {
            recommendedPlan = "A";
            recommendedPrice = 49;
        } else if (talkMinutes < 500 && textMessages > 0 && dataUsage == 0) {
            recommendedPlan = "B";
            recommendedPrice = 55;
        } else if (talkMinutes >= 500 && textMessages < 100 && dataUsage == 0) {
            recommendedPlan = "C";
            recommendedPrice = 61;
        } else if (talkMinutes >= 500 && textMessages >= 100 && dataUsage == 0) {
            recommendedPlan = "D";
            recommendedPrice = 70;
        } else if (dataUsage < 3) {
            recommendedPlan = "E";
            recommendedPrice = 79;
        } else {
            recommendedPlan = "F";
            recommendedPrice = 87;
        }

        // Display the recommended plan to the user
        System.out.println("Based on your needs, we recommend plan " + recommendedPlan + " for $" + recommendedPrice + "/month.");
    }
}
