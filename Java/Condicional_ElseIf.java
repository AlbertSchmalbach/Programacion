public class Condicional_ElseIf {
    public static void main(String[] args) {
        double nota = 7.53;

        if (nota == 10.0) {
            System.out.println("Excelente");
        }else if (nota >= 7.0 && nota < 9.99) {
            System.out.println("Buena");
        }else if (nota >= 6.0 && nota < 7.0) {
            System.out.println("Regular");
        } else {
            System.out.println("Insuficiente");
        }

        // Operador ternario
        int age = 25;

        String result = (age >= 18)? "Mayor de edad": "Menor de edad";

        System.out.println(result);
    
    }
 }


