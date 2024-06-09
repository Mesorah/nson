class Atacar:
    def __init__(self, spawna_mob):
        # Inicializa a classe Atacar recebendo uma instância da classe SpawnaMob como parâmetro
        self.spawna_mob = spawna_mob

    def verifica_posicao(self):
        # Método para verificar a posição do jogador em relação aos monstros
        for posicao in range(len(self.spawna_mob.movimentando.blocos) - 1):
            # Percorre os blocos do jogo até o penúltimo bloco
            if 'a' in self.spawna_mob.movimentando.blocos[posicao]:
                # Verifica se há o jogador ('a') no bloco atual
                if 'm' in self.spawna_mob.movimentando.blocos[posicao + 1]:
                    # Verifica se há um monstro ('m') no próximo bloco
                    self.ataca(posicao + 1)  # Chama o método ataca() passando a posição do monstro

    def ataca(self, posicao):
        # Método para atacar um monstro na posição fornecida
        self.spawna_mob.movimentando.blocos[posicao].pop()  # Remove o monstro do bloco



if __name__ == '__main__':
    atc = Atacar()
    atc.verifica_posicao()