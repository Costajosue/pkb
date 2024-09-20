public class ProjetoTratametoExcecao {

    @SuppressWarnings("static-access")
    public static void main(String[] args) {
        
        /* 
        diminuiLetras ltpqn = new diminuiLetras(); //Chamando classe e criando um objeto//
        ltpqn.lowCase();
        */

        try {
            diminuiLetras ltpqn = new diminuiLetras();
            ltpqn.lowCase();
        } catch (NullPointerException e) {
            System.out.println("Exceção NullPointerException indentificada");
            System.out.println("Metodo diminuiLetras() tratado\n" +e);
        }
    }
}