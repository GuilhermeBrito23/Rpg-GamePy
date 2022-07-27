import Class.PlayerHero
import Class.Monsters
def Exibe_Menu():
    print('*************RPG GAME*************')
    print('1- Começar o Jogo')
    print('2- Ver status do seu personagem')
    print('3- Ver Fila de monstro')
    print('S- Sair')
    print('Selecione uma opção')
def GameStart(hero,monsters):

    while monsters.died == False:
        print('Ambos Atacaram!')
        hero_dmg = hero.Attack()
        monster_dmg = monsters.Attack()
        hero.TakeDamage(monster_dmg)
        monsters.TakeDamage(hero_dmg)
        hero.ShowHero()
        monsters.Died()
        if monsters.died == True:
            print('O monstro morreu!')
            hero.LevelUp(monsters.Died())
        else:
            monsters.ShowMonster()
        input('Tecle enter para continuar')


hero = Class.PlayerHero.PlayerHero()
monster = Class.Monsters.Monsters()
sair = False
op = ''
while sair == False:
    Exibe_Menu()
    op = input().lower().strip()
    match op:
        case '1':
            GameStart(hero,monster)
            break
        case '2':
            hero.ShowHero()
        case '3':
            for i in monsters:
                i.ShowMonster()
            input('Aperte Enter para sair')
        case 's':
           sair = True
           print('Saindo...')

