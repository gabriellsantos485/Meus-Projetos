
class Cadastro():
    """
    Cadastro: Cadastrar produtos variados

    Atributos:

    nome_pessoa(str): nome da pessoa que está cadastrando
    email(str): email da pessoa que está cadastrando
    lista_nomes(str) = lista com nomes dos produtos
    lista_descricao(str): lista com as descricoes dos produtos
    lista_de_valores(int): lista com os valores dos produtos
    produtos_disponiveis(str): listagem com os produtos que estão em estoque
    produtos_sem_estoque(str): listagem com os produtos sem estoque
    """

    def __init__(self, nome_pessoa, email):
        self.nome_pessoa = nome_pessoa
        self.email = email
        self.lista_nomes = []
        self.lista_descricao = []
        self.lista_de_valores = []
        self.produtos_disponiveis = []
        self.produtos_sem_estoque = []

    def cadastrar_produto(self):
        """
        Método para cadastrar um novo produto dentro das listas:
        lista_descricao,
        lista_nomes,
        lista_de_valores,
        produtos_disponiveis,
        produtos_sem_estoque
        :return:
        """
        cadastro = input("Deseja cadastrar um produto ? Digite 'Sim' para prosseguir!")
        while cadastro == 'Sim'or cadastro == 'sim':
            self.nome_produto = input("Digite o nome do produto que deseja cadastrar")
            self.lista_nomes.append(self.nome_produto)
            self.descricao_produto = input("Digite a descrição do produto")
            self.lista_descricao.append(self.descricao_produto)
            valor = input("Digite o valor do produto")
            self.lista_de_valores.append(valor)
            disponibilidade = input("Digite 'S' para disponível para venda ou 'N' para indiponível")
            for produto in self.lista_nomes:
                if disponibilidade == 'S':
                    self.produtos_disponiveis.append(produto)
                if disponibilidade == 'N':
                    self.produtos_sem_estoque.append(produto)
            stop = input("Digite 'S' para sair !")
            if stop == 'S':
                break
        else:
            print('Obrigado tenha um ótimo dia')
    def consultar_produtos(self):
        """
        Método de consulta
        :return:
        """
        tamanho_lista_nomes = len(self.lista_nomes)
        for i in range(tamanho_lista_nomes):
            print('Produto:{}\nDescrição: {}\nValor:R$ {}'.format(self.lista_nomes[i], self.lista_descricao[i], self.lista_de_valores[i]))
            print('-' * 20)








cadastro_produtos_limpeza = Cadastro('gabriel', 'gabriel.santos45987@gmail.com')

cadastro_produtos_limpeza.cadastrar_produto()
print('-' * 20)
cadastro_produtos_limpeza.consultar_produtos()



