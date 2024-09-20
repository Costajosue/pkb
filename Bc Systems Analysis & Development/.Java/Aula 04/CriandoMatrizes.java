public class CriandoMatrizes {

    public static void main(String[] args){
        double mat[][] = {{1.5, 5.2},{3.6, 4.9}, {2.4, 8.1}};
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                System.out.println("M[" +i+ "][" +j+ "]: " + mat[i][j]);
            }
        }
    }
}