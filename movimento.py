from main import Main

class Movimenta:
    def __init__(self, main):
        self.main = main

    def movimentar(self, direcao):
        if not isinstance(direcao, str):
            print('erro')

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
            print('erro')