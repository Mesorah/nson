from atacar import *  # Importando as classes necessárias
from movimentando import Movimentar
from spawna_mob import SpawnaMob
from atacar import Atacar

class Main:
    def __init__(self):
        # Inicialização das instâncias das classes
        self.movimento = Movimentar()  # Instância da classe Movimentar
        self.spawna_mob = SpawnaMob(self.movimento)  # Instância da classe SpawnaMob, passando a instância de Movimentar como parâmetro
        self.ataque = Atacar(self.spawna_mob)  # Instância da classe Atacar, passando a instância de SpawnaMob como parâmetro

    def ver(self):
        return self.movimento.testand()  # Retorna o resultado do método testand() da classe Movimentar

    def direita(self):
        self.movimento.movimentar('d')  # Chama o método movimentar() da classe Movimentar passando 'd' como direção

    def esquerda(self):
        self.movimento.movimentar('e')  # Chama o método movimentar() da classe Movimentar passando 'e' como direção
    
    def verficando_chance(self):
        self.spawna_mob.verfica_chance()  # Chama o método verfica_chance() da classe SpawnaMob para verificar a chance de spawn de monstros

    def atacar_monstro(self):
        self.ataque.verifica_posicao()  # Chama o método verifica_posicao() da classe Atacar para atacar monstros

    def printar_informacoes(self):
        # Imprime informações sobre o jogo
        print('''
Neste jogo você tem que avançar e matar os monstros''')
        print('Boa sorte!')

    def printar_escolhas(self):
        # Imprime as opções disponíveis para o jogador
        print('''
[1] Para se movimentar para a direita
[2] Para se movimentar para a esquerda
[3] Para atacar os monstros''')
        
    def exibe_prints(self):
        # Chama métodos para imprimir informações e opções
        self.printar_informacoes()
        self.printar_escolhas()

    def escolhas(self):
        # Mostra informações e opções e gerencia a escolha do jogador
        self.exibe_prints()
        while True:
            self.ver()  # Mostra a situação atual do jogo
            acao = input('O que fazer? ')  # Solicita ação do jogador
            self.verficando_chance()  # Verifica a chance de spawn de monstros

            if not acao.isdigit():
                print('Opção inválida')  # Mensagem de erro se a entrada não for um número

            else:
                if int(acao) == 1:
                    self.direita()  # Movimenta para a direita
                elif int(acao) == 2:
                    self.esquerda()  # Movimenta para a esquerda
                elif int(acao) == 3:
                    self.atacar_monstro()  # Ataca os monstros

main = Main()  # Instância da classe Main
main.escolhas()  # Inicia o jogo