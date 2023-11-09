// explicación : https://www.techiedelight.com/es/introduction-priority-queues-using-binary-heaps/
// implementación: https://www.techiedelight.com/es/min-heap-max-heap-implementation-in-java/ 

// add() , poll()                 O(log(n))
// toArray() , contains()         O(n)
// peek() , size() , isEmpty()    O(1)




import java.util.Arrays;
import java.util.Vector;
 
// Una clase para implementar la cola de prioridad
class PriorityQueue
{
    // vector para almacenar elementos de heap
    private Vector<Integer> A;
 
    // constructor: usa la capacidad inicial por defecto de un vector
    public PriorityQueue() {
        A = new Vector();
    }
 
    // constructor: establece una capacidad inicial personalizada para el vector
    public PriorityQueue(int capacity) {
        A = new Vector(capacity);
    }
 
    // devuelve el padre de `A[i]`
    private int parent(int i)
    {
        // si `i` ya es un nodo raíz
        if (i == 0) {
            return 0;
        }
 
        return (i - 1) / 2;
    }
 
    // devuelve el hijo izquierdo de `A[i]`
    private int LEFT(int i) {
        return (2*i + 1);
    }
 
    // devuelve el hijo derecho de `A[i]`
    private int RIGHT(int i) {
        return (2*i + 2);
    }
 
    // intercambiar valores en dos índices
    void swap(int x, int y)
    {
        // intercambio con un niño que tiene mayor valor
        Integer temp = A.get(x);
        A.setElementAt(A.get(y), x);
        A.setElementAt(temp, y);
    }
 
    // Procedimiento recursivo de heapify-down. Aquí, el nodo en el índice `i`
    // y sus dos hijos directos violan la propiedad del heap
    private void heapify_down(int i)
    {
        // obtener el hijo izquierdo y derecho del nodo en el índice `i`
        int left = LEFT(i);
        int right = RIGHT(i);
 
        int smallest = i;
 
        // compara `A[i]` con su hijo izquierdo y derecho
        // y encontrar el valor más pequeño
        if (left < size() && A.get(left) < A.get(i)) {
            smallest = left;
        }
 
        if (right < size() && A.get(right) < A.get(smallest)) {
            smallest = right;
        }
 
        if (smallest != i)
        {
            // intercambio con un niño que tiene un valor menor
            swap(i, smallest);
 
            // llama a heapify-down en el hijo
            heapify_down(smallest);
        }
    }
 
    // Procedimiento heapify-up recursivo
    private void heapify_up(int i)
    {
        // comprueba si el nodo en el índice `i` y su padre violan
        // la propiedad del heap
        if (i > 0 && A.get(parent(i)) > A.get(i))
        {
            // intercambiar los dos si se viola la propiedad del heap
            swap(i, parent(i));
 
            // llama a heapify-up en el padre
            heapify_up(parent(i));
        }
    }
 
    // devuelve el tamaño del heap
    public int size() {
        return A.size();
    }
 
    // comprobar si el heap está vacío o no
    public Boolean isEmpty() {
        return A.isEmpty();
    }
 
    // inserta una clave específica en el heap
    public void add(Integer key)
    {
        // inserta un nuevo elemento al final del vector
        A.addElement(key);
 
        // obtener su índice y llamar al procedimiento heapify-up
        int index = size() - 1;
        heapify_up(index);
    }
 
    // Función para eliminar y devolver un elemento con la prioridad más alta
    // (presente en la raíz). Devuelve nulo si la queue está vacía
    public Integer poll()
    {
        try {
            // si el heap está vacío, lanza una excepción
            if (size() == 0) {
                throw new Exception("Index is out of range (Heap underflow)");
            }
 
            // elemento con la mayor prioridad
            int root = A.firstElement();    // o A.get(0);
 
            // reemplaza la raíz del heap con el último elemento del vector
            A.setElementAt(A.lastElement(), 0);
            A.remove(size() - 1);
 
            // llama a heapify-down en el nodo raíz
            heapify_down(0);
 
            // devuelve el elemento raíz
            return root;
        }
        // captura e imprime la excepción
        catch (Exception ex)
        {
            System.out.println(ex);
            return null;
        }
    }
 
    // Función para devolver un elemento con la prioridad más alta
    // (presente en la raíz). Devuelve nulo si la queue está vacía
    public Integer peek()
    {
        try {
            // si el heap no tiene elementos, lanza una excepción
            if (size() == 0) {
                throw new Exception("Index out of range (Heap underflow)");
            }
 
            // de lo contrario, devuelve el elemento superior (primero)
            return A.firstElement();    // o A.get(0);
        }
        // captura la excepción, la imprime y devuelve nulo
        catch (Exception ex)
        {
            System.out.println(ex);
            return null;
        }
    }
 
    // Función para eliminar todos los elementos de la cola de prioridad
    public void clear()
    {
        System.out.print("Emptying queue: ");
        while (!A.isEmpty()) {
            System.out.print(poll() + " ");
        }
        System.out.println();
    }
 
    // Devuelve verdadero si la queue contiene el elemento especificado
    public Boolean contains(Integer i) {
        return A.contains(i);
    }
 
    // Devuelve una array que contiene todos los elementos de la queue
    public Integer[] toArray() {
        return A.toArray(new Integer[size()]);
    }
}
 
class Main
{
    public static void main (String[] args)
    {
        // crea una cola de prioridad con una capacidad inicial de 10.
        // El valor de un elemento decide la prioridad del mismo.
        PriorityQueue pq = new PriorityQueue(10);
 
        // inserta tres enteros
        pq.add(3);
        pq.add(2);
        pq.add(15);
 
        // tamaño de la cola de prioridad de impresión
        System.out.println("Priority queue size is " + pq.size());
 
        // busca 2 en la cola de prioridad
        Integer searchKey = 2;
 
        if (pq.contains(searchKey)) {
            System.out.println("Priority queue contains " + searchKey + "\n");
        }
 
        // queue vacía
        pq.clear();
 
        if (pq.isEmpty()) {
            System.out.println("The queue is empty");
        }
 
        System.out.println("\nCalling remove operation on an empty heap");
        System.out.println("The element with the highest priority is " + pq.poll());
 
        System.out.println("\nCalling peek operation on an empty heap");
        System.out.println("The element with the highest priority is " + pq.peek() +
                    System.lineSeparator());
 
        // inserta nuevamente tres enteros
        pq.add(5);
        pq.add(4);
        pq.add(45);
 
        // construye una array que contiene todos los elementos presentes en la queue
        Integer[] I = pq.toArray();
        System.out.println("Printing array: " + Arrays.toString(I));
 
        System.out.println("\nThe element with the highest priority is " + pq.poll());
        System.out.println("The element with the highest priority is " + pq.peek());
    }
}