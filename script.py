
class Pokemon:
    type_chart = ['Fire', 'Water', 'Grass']
    tip_chart = ['Water', 'Grass', 'Fire']
    t_chart = ['Grass', 'Fire', 'Water']
    damage = 0

    def __init__(self, name, level, typeth, max_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.type = typeth
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out
        
    def lose_health(self, amount):
        self.current_health -= amount
        print('{} currently has {} health'.format(self.name, self.current_health))

    def regain_health(self, amount):
        self.current_health += amount
        print('{} currently has {} health'.format(self.name, self.current_health))

    def check_knock(self):
      if self.current_health <= 0:
        self.knocked_out = True
      if self.knocked == True:
        print("{} is knocked out".format(self.name))
      else:
        print("{} is healthy".format(self.name))

    def attack(self, other_pokemon):
      if self.knocked_out == True:
        print("You can't attack with a knocked out Pokemon.")
      else:
        self.damage = self.level * 2
        if self.type_chart.index(self.type) == self.tip_chart.index(other_pokemon.type):
          self.damage = self.damage/2
          print('That wasnt very effective')
        elif self.type_chart.index(self.type) == self.t_chart.index(other_pokemon.type):
          self.damage = self.damage * 2
          print('That was super-effective')
        other_pokemon.current_health -= self.damage
        print('The {} has taken {} damage and now has {} health.'.format(other_pokemon.name, str(self.damage), str(other_pokemon.current_health)))
        if other_pokemon.current_health <= 0:
          other_pokemon.knocked_out = True
      
        

char = Pokemon('Charmander', 10, 'Fire', 30, 30, False)
bulb = Pokemon('Bulbasaur', 10, 'Grass', 30, 30, False)
squi = Pokemon('Squirtle', 10, 'Water', 30, 30, False)


class Trainer:
  def __init__(self, name, potions, pokemons, current_pokemon):
    self.name = name
    self.potions = potions
    self.pokemons = pokemons
    self.current_pokemon = current_pokemon

  def use_potion(self):
    self.potions -= 1
    if self.pokemons[self.current_pokemon].current_health >= self.pokemons[self.current_pokemon].max_health:
      print("You can't heal any more")
    else:  
      self.pokemons[self.current_pokemon].current_health += 20
      print('You now have {} potions left.'.format(str(self.potions)))
      print('{} now has {} health.'.format(self.pokemons[self.current_pokemon].name, str(self.pokemons[self.current_pokemon].current_health)))

  def attack(self, other_trainer):
    self.pokemons[self.current_pokemon].attack(other_trainer.pokemons[other_trainer.current_pokemon])
    if self.pokemons[self.current_pokemon].damage > 0:
      print('Your {} deals {} points of damage. The {} now has {} health left.'.format((self.pokemons[self.current_pokemon].name), str(self.pokemons[self.current_pokemon].damage), other_trainer.pokemons[other_trainer.current_pokemon].name, str(other_trainer.pokemons[other_trainer.current_pokemon].current_health)))

  def switch_pokemon(self, target_pokemon):
    self.current_pokemon = self.pokemons.index(target_pokemon)
    print('You have switched to {}'.format(self.pokemons[self.current_pokemon].name))

alex = Trainer('Alex', 3, [char, bulb], 0)
steve = Trainer('Steve', 5, [squi], 0)


alex.attack(steve)
alex.attack(steve)
alex.attack(steve)

steve.attack(alex)
