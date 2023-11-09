public class AlgoritmosDeBusquedaYOrdenamiento {

    public static void main(String[] args){

        int[] vectorOrdenadoSinRepetidos = {-2,-1,3,7,9,15};
        int numBuscado = 9;

    
        int res = busquedaBinaria(vectorOrdenadoSinRepetidos, numBuscado); // busqueda binaria O(log n)
        System.out.println(res);
    }


    private static int sumar(int x , int y){
        return(x+y);
    }

    


    public static int busquedaBinaria(int [] array, int numeroBuscado) {
        int result = -1; // El indice resultado comienza siendo -1
        int limiteInferior = 0;
        int limiteSuperior = array.length - 1;
        int indice;
                     
        while (limiteInferior <= limiteSuperior && result == -1) { // El while termina cuando los limites se cruzan
            
            indice = (limiteInferior + limiteSuperior) / 2; // En cada vuelta, el indice es (LI+LS)/2
                 
            if (array[indice] == numeroBuscado) {    // Chequeo si numeroBuscado = array[indice] 
                System.out.println("Encontrado");
                result = indice;
            }

            
            if (numeroBuscado > array[indice]) { // Si numeroBuscado > array[indice]
                limiteInferior = indice + 1;     // Muevo el piso hacia la derecha 1 unidad
            }
            
            if (numeroBuscado < array[indice]) { // Si numeroBuscado < array[indice]
                limiteSuperior = indice - 1;     // Muevo el techo hacia la izquierda 1 unidad
            }
        }
             
        return result; // Cuando finalice el while, o retorno el -1 o retorno el indice

    }    
       

    
} 
