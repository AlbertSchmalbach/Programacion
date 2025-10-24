package platzi.play;

import platzi.play.contenido.Pelicula;
import platzi.play.plataforma.Plataforma;
import platzi.play.plataforma.Usuario;
import platzi.play.util.ScannerUtils;

public class Main {

    public static final String NOMBRE_PLATAFORMA = "PLATZI PLAY 🍿 ";
    public static final String VERSION = "1.0.0";



    public static void main(String[] args) {
        System.out.println(NOMBRE_PLATAFORMA + " v" + VERSION);

        Plataforma plataforma = new Plataforma(NOMBRE_PLATAFORMA);

        String nombre = ScannerUtils.capturarTexto("Nombre del contenido");
        String genero = ScannerUtils.capturarTexto("Genero del contenido");
        int duracion = ScannerUtils.capturarNumero("Duracion del contenido");
        double calificacion = ScannerUtils.capturarDecimal("Calificacion del contenido");

        Pelicula peli1 = new Pelicula(nombre, duracion, genero);
        Pelicula peli2 = new Pelicula(nombre, duracion, genero);

        plataforma.agregar(peli1);
        plataforma.agregar(peli2);
        System.out.println("Numero de elementos en plataforma: " + plataforma.getContenido().size());

        peli1.calificar(calificacion);
        System.out.println(peli1.obtenerFichaTecnica());

//        long duracionLong = peli1.duracion;
//        int calificacionInt = (int) peli1.calificacion;
//        long numeroPremios = (int) Long.parseLong("25");

        Usuario user1 = new Usuario("Luz Saray", "luzatenciam@gmail.com");
        System.out.println("Usuario: " + user1.nombre);
        System.out.println("Fecha de registro de usuario: " + user1.fechaRegistro);
        user1.ver(peli1);
//        System.out.println("Duracion: " + duracionLong);
//        System.out.println("Calificacion int: " + calificacionInt);
//        System.out.println("Premios: " + numeroPremios);




    }
}
