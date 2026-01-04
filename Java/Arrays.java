public class Arrays {
    public static void main(String[] args) {

        int [] myArray = new int[5];

        myArray[0] = 5;
        myArray[1] = 12;
        myArray[2] = 28;
        myArray[3] = 90;
        myArray[4] = 7;

        System.out.println(myArray);

        // int[] myArray2 = {15, 20, 30, 16, 2};

        for (int i = 0; i < myArray.length; i++) {
            System.out.println(myArray[i]);
        }

        
    }
}
