class Animals:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_name(self):
        return self.name

    def get_info(self):
        return f'Name: {self.name}, population: {self.population}'

    def set_population(self, population):
        print('Set new population')
        self.population = population


class Mammals(Animals):
    def __init__(self, name, population, is_herbivore):
        super().__init__(name, population)
        self.is_herbivore = is_herbivore

    def get_info(self):
        return f'Name: {self.name}, population: {self.population}, herbivore: {self.is_herbivore}'


class Amphibias(Animals):
    def __init__(self, name='Frog', population=100):
        super().__init__(name, population)

    def add_population(self, population):
        self.population += population
        print(f'Now the population = {self.population}')

    def sub_population(self, population):
        self.population -= population
        print(f'Now the population = {self.population}')


if __name__ == '__main__':
    animal = Animals('Elephant', 1500)
    mammal = Mammals('Bear', 2000, False)
    amphibia = Amphibias()

    animal.set_population(1000)
    print(animal.get_info())

    print(mammal.get_info())

    amphibia.add_population(100)
    amphibia.sub_population(50)
    print(amphibia.get_info())
