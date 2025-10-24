package platzi.play;

import platzi.play.contenido.Pelicula;

public class MeanStackHeap {
    public static void main(String[] args) {
        Pelicula reyLeon = new Pelicula("El Rey Leon", 135, "Animada");
        Pelicula harryPotter = new Pelicula("Harry Potter", 200, "fantasia");

        reyLeon = harryPotter;
//
//        reyLeon.titulo = "El Hobbit";
//
//        System.out.println(reyLeon.titulo);
//        System.out.println(harryPotter.titulo);
    }
}
