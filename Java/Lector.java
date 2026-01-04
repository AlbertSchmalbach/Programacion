import java.util.Scanner;

public class Lector {
    public static void main(String[] args) {
        String nombrePersona;
        int edad;

        Scanner in = new Scanner(System.in);

        System.out.print("Cual es tu nombre: ");
        nombrePersona = in.nextLine();

        System.out.print("Edad: ");
        edad = in.nextInt();

        System.out.println("Hola " + nombrePersona + ", tu edad es " + edad + " de años." );
    }
}
