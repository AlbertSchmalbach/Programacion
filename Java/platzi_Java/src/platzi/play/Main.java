package platzi.play;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("PLATZI PLAY");

        Scanner sc = new Scanner(System.in);
        System.out.print("Nombre: ");
        String nombre = sc.nextLine();

        System.out.println("Hola " + nombre + " esto es PLATZI PLAY!"
        );

        System.out.print(nombre + ", Cuantos años tienes? ");
        int age = sc.nextInt();

        System.out.println(nombre + ", puedes ver mas " + age);
    }
}
