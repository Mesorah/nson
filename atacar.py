class Atacar:
    def __init__(self, spawna_mob):
        self.spawna_mob = spawna_mob


    def verifica_posicao(self):
        for posicao in range(len(self.spawna_mob.movimentando.blocos) - 1):
                if 'a' in self.spawna_mob.movimentando.blocos[posicao]:

                    if 'm' in self.spawna_mob.movimentando.blocos[posicao + 1]:
                        self.ataca(posicao + 1)
    
    def ataca(self, posicao):
        self.spawna_mob.movimentando.blocos[posicao].pop()



if __name__ == '__main__':
    atc = Atacar()
    atc.verifica_posicao()