public class Buleanos {
    public static void main(String[] args) {
        System.out.println(10 > 5);
        int x = 5;
        System.out.println(x == 10);

        int myAge = 25;
        int votingAge = 18;
        System.out.println(myAge >= votingAge);

        if (myAge >= votingAge) {
            System.out.println("Puedes votar");
        }

        if (20 > 5)
            System.out.println("Si es mayor");

        int m = 20;
        int n = 18;

        if (m > n)
            System.out.println("x is greater than y"); // Belongs to if
            System.out.println("This line runs no matter what (not part of the if statement)");

        int time = 35;

        if (time >= 25) {
            System.out.println("clima caliente");
        } else {
            System.out.println("Clima frio");
        }
    }

    
}
