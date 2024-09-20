import java.util.Iterator;

@SuppressWarnings("unused")
public class Servicos {
    //Encapsulamento dos atributos
    private int id;
    private String TipoServico;
    private double Preco;

    public int getld(){
        return id;
    }
    public String getTpServico(){
        return TipoServico;
    }
    public double getPreco(){
        return Preco;
    }

    public void setid(int id){
        this.id = id;
    }

    public void setTpServico(String getTpServico){
        this.TipoServico = getTpServico;
    }

    public void setPreco(double Preco){
        this.Preco = Preco;
    }
}
