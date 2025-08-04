import java.util.Scanner;

public class NumeroMayor {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        System.out.print("Ingresa el primer numero: ");
        int num1 = in.nextInt();
        System.out.print("Ingresa el segundo numero:");
        int num2 = in.nextInt();

        boolean numMayor = num1 == num2;

        System.out.println(numMayor);
    }
}
