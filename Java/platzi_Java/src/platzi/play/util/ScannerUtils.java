package platzi.play.util;

import java.util.Scanner;

public class ScannerUtils {
    public  static final Scanner SC = new Scanner(System.in);

    public static String capturarTexto(String mensaje){
        System.out.println(mensaje + ": ");
        return SC.nextLine();
    }

    public static int capturarNumero(String mensaje){
        System.out.println(mensaje + ": ");
        int dato = SC.nextInt();
        SC.nextLine();
        return dato;
    }

    public static double capturarDecimal(String mensaje){
        System.out.println(mensaje + ": ");
        double dato = SC.nextDouble();
        SC.nextLine();
        return dato;
    }
}
