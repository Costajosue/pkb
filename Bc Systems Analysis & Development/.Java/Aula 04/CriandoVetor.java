/*A linguagem Java permite a criação de arrays
unidimensionais também chamados de vetores. Umvetor
agrupa um conjunto de dados de um mesmo tipo
organizados em linha ou coluna, e por trabalhar comdados do mesmo tipo, falamos que o vetor é uma
estrutura de dados homogênea.*/

public class CriandoVetor {
    public static void main(String args[]){
        int vet[] = new int[5];
        
        vet[0] = 5;
        vet[1] = 6;
        vet[2] = 7;
        vet[3] = 8;
        vet[4] = 9;

        for(int i = 0; i < vet.length; i ++){
            System.out.println(" vetor na posição [" + i +"]" +vet[i]);
        }
    }
}
