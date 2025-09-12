public class Math_Java {

    public static void main(String[] args) {
        // Math.max()
        System.out.println("Max: " + Math.max(15, 10));
        System.out.println("Min: " + Math.min(15, 10));

        // Math.sqrt()
        System.out.println("Raiz: " + Math.sqrt(64));

        // Math.abs()
        System.out.println("Valor Absoluto: " + Math.abs(-4.7));

        // Math.random()
        System.out.println("Random: " + Math.random());
        int randomNum = (int)(Math.random()*101);
        System.out.println("Aleatorio: " + randomNum);
    }
}