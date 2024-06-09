from atacar import *
from movimentando import Movimentar
from spawna_mob import SpawnaMob
from atacar import Atacar

class Main:
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


    def atacar_monstro(self):
        self.ataque.verifica_posicao()


    def printar_informacoes(self):
        print('''
Neste jogo você tem que avançar e matar os monstros''')
        print('Boa sorte!')

    
    def printar_escolhas(self):
        print('''
[1] Para se movimentar para a direita
[2] Para se movimentar para a esquerda
[3] Para atacar os monstrons''')
        

    def exibe_prints(self):
        self.printar_informacoes()
        self.printar_escolhas()


    def escolhas(self):
        self.exibe_prints()
        while True:
            self.ver()
            acao = input('O que fazer? ')
            self.verficando_chance()

            if not acao.isdigit():
                print('Opção inválida')

            else:
                if int(acao) == 1:
                    self.direita()

                elif int(acao) == 2:
                    self.esquerda()

                elif int(acao) == 3:
                    self.atacar_monstro()
                

main = Main()
main.escolhas()
