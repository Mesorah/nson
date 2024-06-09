from random import randint

class SpawnaMob:
    def __init__(self, movimentando):
        # Inicializa a lista de chances e recebe a instância da classe Movimentar
        self.lista_chances = [1, 2, 3]
        self.movimentando = movimentando

    def chance_spawn(self):
        # Retorna um número aleatório entre 1 e 10
        return randint(1, 10)

    def verfica_chance(self):
        # Verifica se a chance de spawn de monstro ocorre
        if self.chance_spawn() in self.lista_chances:
            self.spawna_mob()  # Chama o método spawna_mob() se a chance ocorrer
        else:
            pass

    def spawna_mob(self):
        # Adiciona um monstro à lista de blocos na última posição
        for c in range(len(self.movimentando.blocos)):
            if c == 8:
                self.movimentando.blocos[c].append('m')


if __name__ == '__main__':
    sm = SpawnaMob()
    sm.chance_spawn()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()
    sm.verfica_chance()