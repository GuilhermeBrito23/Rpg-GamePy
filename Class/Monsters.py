import random

class Monsters:

    def __init__(self):
        monsters_name = ['Bluezenificado', 'Marquitu', 'Salmonelado', 'Cachaçinha', 'Katapimbas',
                         'Palma da Bota']
        rand = random.randrange(0,len(monsters_name))
        self.name = monsters_name[rand]
        self.__max_hp = 20
        self.__hp = 20
        self.__exp = 100
        self.__power = 1.0
        self.died = False

    def ShowMonster(self):
        print('---------------------')
        print('Nome: {}'.format(self.name))
        print('HP: {}/{}'.format(self.__hp, self.__max_hp))
        print('Exp: {}'.format(self.__exp))
        print('Força: {}'.format(self.__power))

    def Attack(self):
        rand = random.randrange(0,3)
        match rand:
            case 0:
                rand_dmg = random.randrange(1,11)
                return self.__power * rand_dmg
            case 1:
                rand_dmg = random.randrange(11, 21)
                return self.__power * rand_dmg
            case 2:
                rand_dmg = random.randrange(21, 31)
                return self.__power * rand_dmg

    def TakeDamage(self,dmg):
        self.__hp -= dmg

    def Died(self):
        if self.__hp <= 0:
            self.died = True
            return self.__exp

