import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class MapDemo 
{

    public static void main(String[] args) 
    {
        HashMap<Integer, String> hmap = new HashMap<>();
        Scanner in = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            Integer a = in.nextInt();
            String b = in.next();

            hmap.put(a, b);
        }

        for (Map.Entry<Integer, String> m : hmap.entrySet()) 
        {
            System.out.println(m.getKey() + " " + m.getValue());
        }
    }
}
