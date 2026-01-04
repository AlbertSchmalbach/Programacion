import java.util.Scanner;

public class CalculoSimple {
    public static void main(String[] args) {
        int largo, ancho, area, perimetro;
        double radio, areaCirculo, perCirculo;
        final double pi = 3.1415;

        Scanner in = new Scanner(System.in);

        System.out.print("Ingresa largo del rectangulo: ");
        largo = in.nextInt();

        System.out.print("Ingresa ancho del rectangulo: ");
        ancho = in.nextInt();

        System.out.print("Ingresa el radio de la circunferencia: ");
        radio = in.nextDouble();

        area = largo * ancho;
        perimetro = 2 * (largo + ancho);

        areaCirculo = pi * (Math.pow(radio, 2));
        perCirculo = 2 * pi * radio;

        System.out.println("El area del rectangulo es " + area);
        System.out.println("El perimetro del rectangulo es " + perimetro);
        System.out.println();
        System.out.println("El area del circulo es " + areaCirculo);
        System.out.println("El perimetro del circulo es " + perCirculo);
    }
}
