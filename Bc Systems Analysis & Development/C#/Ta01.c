int main(int argc, char** argv) {

    char nome [30];
    char endereco[30];
    int idade;

    printf("nome \n");
    scanf("%s", &nome);

    printf("endereco \n");
    scanf("%s", &endereco);

    printf("idade");
    scanf("%d", &idade);
    
    printf("\n Nome: %s", nome);
    printf("\n endereco: %s", endereco);
    printf("\n idade: %d", idade);

}