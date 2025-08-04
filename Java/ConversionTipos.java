public class ConversionTipos {
    public static void main(String[] args) {

        // Casting automatico
        int myInt = 10;
        double myDouble = myInt;

        System.out.println(myInt);
        System.out.println(myDouble);

        // Casting Manual
        double number = 3.14d;
        int myNumber = (int) number;

        System.out.println(myNumber);

        // Example:
        
        // Set the maximum possible score in the game to 500
        int maxScore = 500;

        // The actual score of the user
        int userScore = 423;

        /*
         * Calculate the percentage of the user's score in relation to the maximum
         * available score.
         * Convert userScore to float to make sure that the division is accurate
         */
        float percentage = (float) userScore / maxScore * 100.0f;

        System.out.println("User's percentage is " + percentage);
    }
}
