from atacar import *
from movimentando import Movimentar
from spawna_mob import SpawnaMob
from atacar import Atacar

class Teste:
    def __init__(self):
        self.movimento = Movimentar()
        self.spawna_mob = SpawnaMob(self.movimento)
        self.ataque = Atacar(self.spawna_mob)


    def ver(self):
        return self.movimento.testand()
    

    def direita(self):
        self.movimento.movimentar('d')


    def esquerda(self):
        self.movimento.movimentar('e')

    
    def verficando_chance(self):
        self.spawna_mob.verfica_chance()


    def spawnar_monstro(self):
        self.spawna_mob.spawna_mob()

    def atacar_monstro(self):
        self.ataque.verifica_posicao()


if __name__ == '__main__':
    test = Teste()
    test.ver()
    test.direita()
    test.direita()
    test.direita()
    test.direita()
    test.direita()
    test.direita()
    test.direita()
    test.verficando_chance()
    test.spawnar_monstro()
    test.ver()
    test.atacar_monstro()
    test.ver()