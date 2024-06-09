from random import randint

class SpawnaMob:
    def __init__(self, movimentando):
        self.lista_chances = [1, 2, 3]
        self.movimentando = movimentando


    def chance_spawn(self):
        return randint(1, 10)
    

    def verfica_chance(self):
        if self.chance_spawn() in self.lista_chances:
            self.spawna_mob()
        
        elif self.chance_spawn() not in self.lista_chances:
            pass

    def spawna_mob(self):
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