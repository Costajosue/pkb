import javax.swing.JOptionPane;

public class MostrarServicos {
    public static void main(String[] args) {
        //define a quantidade de posições do array
        Servicos[]precoMaior;
        precoMaior = new Servicos[5];
        Servicos exibeMetodos = new Servicos();

        for (int i = 0; i < 5; i++){
            precoMaior[i] = new Servicos();
            precoMaior[i].setTpServico(JOptionPane.showInputDialog(null, "Informe o " + precoMaior[i].getld() + " Serviço a ser cadastrado"));
            precoMaior[i].setPreco(Double.parseDouble(JOptionPane.showInputDialog(null,"informe o preço do " + precoMaior[i].getld()+"serviço: ")));
        }
    System.out.println(exibeMetodos);

    }
}
