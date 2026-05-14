import java.util.LinkedList;
import java.util.Queue;

public class FilaSimples 
{
    public static void main(String[] args) 
    {
        Queue<String> fila = new LinkedList<>();

        fila.add("Ana");
        fila.add("Bruno");
        fila.add("Carla");

        System.out.println("Primeiro da fila: " + fila.peek());

        String atendido = fila.poll();
        System.out.println("Cliente atendido: " + atendido);

        System.out.println("Fila atual: " + fila);
    }
}