import java.util.Scanner;

public class SumaCifras {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int c1, c2, c3, c4;
        int numCuatroCifras = 0;

        System.out.print("Ingresa un numero de 4 cifras: ");
        numCuatroCifras = in.nextInt();
        in.nextLine();

        c1 = numCuatroCifras % 10;
        c2 = (numCuatroCifras/10)%10;
        c3 = (numCuatroCifras/100)%10;
        c4 = numCuatroCifras/1000;

        int suma = c1 + c2 + c3 + c4;

        System.out.println("La suma de los digitos de la cifra da: " + suma);
    }
}
