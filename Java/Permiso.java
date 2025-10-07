import java.util.Scanner;

public class Permiso {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Departamento: ");
        String departament = scan.nextLine().trim();

        // if (departament.equalsIgnoreCase("bolivar")) {
        //     System.out.print("Ciudad: ");
        //     String city = scan.nextLine().trim();
        //     if (city.equalsIgnoreCase("magangue")) {
        //         System.out.println("Estas en la tierra del bocachico");
        //     } else {
        //         System.out.println("Estas en otra localidad de bolivar");
        //     }
        // } else {
        //     System.out.println("Eres de otra parte de Colombia");
        // }

        System.out.print("Ciudad: ");
        String city = scan.nextLine().trim();
    
        if (departament.equalsIgnoreCase("bolivar") && city.equalsIgnoreCase("magangue")) {
            System.out.println("Estas en la tierra del bocachico");
        } else {
            System.out.println("Estas en otra parte");
        }

        scan.close();
    }
}
