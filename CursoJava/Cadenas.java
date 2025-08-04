public class Cadenas {
    public static void main(String[] args) {
        String txt = "En el principio Dios creo los cielos y la tierra";
        System.out.print("\n");
        // Longitud de la cuerda
        System.out.println("Longitud de cadena: " + txt.length());

        // Más métodos de cadena
        System.out.println(txt.toLowerCase());
        System.out.println(txt.toUpperCase());

        // Encontrar un carácter en una cadena
        System.out.println("Posicion de la palabra 'Dios' en 'txt': " + txt.indexOf("Dios"));

        // Concatenar cadenas
        String name = "Albert";
        String lastName = "Schmalbach";

        System.out.println(name + " " + lastName);
        System.out.println(name.concat(lastName));

    }
}
