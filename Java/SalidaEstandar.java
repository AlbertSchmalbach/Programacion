
import java.util.Scanner;

public class SalidaEstandar {
    public static void main(String[] args) {
        System.out.println();

        String name = "";

        Scanner in = new Scanner(System.in);

        System.out.print("Ingresa tu nombre: ");
        name = in.nextLine();

        System.out.println("Hola " + name + ", bienvenido(a) a Java");
    
    }
}
