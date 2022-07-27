import random
class PlayerHero:
    def __init__(self):
        self.__level = 1
        self.__max_hp = 100
        self.__hp = 100
        self.__max_exp = 100
        self.__exp = 0
        self.__power = 0.5

    def ShowHero(self):
        print('Nivel:{}'.format(self.__level))
        print('HP: {}/{}'.format(self.__hp,self.__max_hp))
        print('Exp: {}/{}'.format(self.__exp, self.__max_exp))
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

    def LevelUp(self,exp):
        self.__exp += exp
        if self.__exp == self.__max_exp:
            self.__level +=1
            self.__max_hp *= 1.5
            self.__hp = self.__max_hp
            self.__max_exp *= 1.5
            self.__exp = 0
            self.__power *= 1.5
            print('Você Subiu de nivel!')
            self.ShowHero()
        if self.__exp > self.__max_exp:
            over_exp = self.__exp - self.__max_exp
            self.__level += 1
            self.__max_hp *= 1.5
            self.__hp = self.__max_hp
            self.__max_exp *= 1.5
            self.__exp = over_exp
            self.__power *= 1.5
            self.ShowHero()
            print('Você Subiu de nivel!')
