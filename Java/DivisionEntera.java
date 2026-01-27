import java.util.Scanner;

public class DivisionEntera {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int cantPelotas, cantNiños;
        int pelotasNiños, pelotaSobrantes;

        System.out.print("Ingresa cantidad de niños y pelotas: ");
        cantNiños = in.nextInt();
        cantPelotas = in.nextInt();
        in.nextLine();

        pelotasNiños = cantPelotas / cantNiños;
        pelotaSobrantes = cantPelotas % cantNiños;

        System.out.println("Pelotas por niños: " + pelotasNiños + " Pelotas sobrantes: " + pelotaSobrantes);



    }
}
