class Movimentar:
    def __init__(self):
        self.blocos = [['a'], [], [], [], [], [], [], [], []]  # Inicializa uma lista de blocos

    def movimentar(self, direcao):
        # Move o jogador para a direita ou esquerda, dependendo da direção fornecida
        if not isinstance(direcao, str):
            print('erro')  # Mensagem de erro se a direção não for uma string
            return

        if direcao[0] == 'd':
            for posicao in range(len(self.blocos) - 1):
                if 'a' in self.blocos[posicao]:
                    self.blocos[posicao].remove('a')
                    self.blocos[posicao + 1].append('a')
                    return

        elif direcao[0] == 'e':
            for posicao in range(len(self.blocos) - 1):
                if 'a' in self.blocos[posicao]:
                    self.blocos[posicao].remove('a')
                    self.blocos[posicao - 1].append('a')
                    return

        else:
            print('erro')  # Mensagem de erro se a direção não for 'd' ou 'e'

    def testand(self):
        # Método para teste que mostra a posição atual do jogador
        print(self.blocos)



if __name__ == '__main__':
    m = Movimentar()
    m.testand()
    m.movimentar('d')
    m.testand()
    m.movimentar('d')
    m.testand()
    m.movimentar('e')
    m.testand()