from random import choice

class Team:

    def __init__(self, name):
        self.name = name
        self.soldiers = []
        self.hero = None

    def add_soldier(self, soldier):
        if isinstance(soldier, Soldier):
            self.soldiers.append(soldier)

    def add_hero(self, hero):
        if isinstance(hero, Hero):
            self.hero = hero

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.soldiers) + 1 if self.hero else len(self.soldiers)

class Hero:

    def __init__(self, name, id, team):
        self.team = team
        self.name = name
        self.id = id
        self.lvl = 0

    def __str__(self):
        return self.name

    def lvl_up(self):
        self.lvl += 1

class Soldier:

    def __init__(self, id, team):
        self.team = team
        self.id = id
        self.hero = None #За кем следует солдат

    def go_to_hero(self, hero):
        if isinstance(hero, Hero):
            self.hero = hero

if __name__ == '__main__':
    red = Team('red')
    blue = Team('blue')
    red.add_hero(Hero('Archer', 1, red))
    blue.add_hero(Hero('Swordsman', 1, blue))
    team_list = [red, blue]

    for i in range(1, int(input('Введите количество солдат: ')) + 1):
        team = choice(team_list)
        team.add_soldier(Soldier(i, team))

    print(f'В красной команде - {len(red)} юнитов, в синей - {len(blue)}')

    if len(red) > len(blue):
        red.hero.lvl_up()
    else:
        blue.hero.lvl_up()

    soldier = red.soldiers[0]
    soldier.go_to_hero(red.hero)
    print(f'Id солдата, следующего за героем: {soldier.id}, Id героя: {soldier.hero.id}')

