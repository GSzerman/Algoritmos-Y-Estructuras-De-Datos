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

    


    public static int busquedaBinaria(int [] items, int numeroBuscado) {
        int result = -1;
        int limiteInferior = 0;
        int limiteSuperior = items.length - 1;
        int indice;
                     
        while (limiteInferior <= limiteSuperior && result == -1) {
            indice = (limiteInferior + limiteSuperior) / 2;
                 
            if (items[indice] == numeroBuscado) {
                System.out.println("Encontrado");
                result = indice;
            }else if (numeroBuscado > items[indice]) {
                limiteInferior = indice + 1;
            }else if (numeroBuscado < items[indice]) {
                limiteSuperior = indice - 1;
            }
        }
             
        return result;
    }    
       

    
} 
