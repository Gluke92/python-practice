class User():
  def sign_in(self):
    return 'logged in'


class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with {self.power}')


class Archer(User):
  def __init__(self, name, arrows):
    self.name = name
    self.arrows = arrows

  def shoot_arrows(self):
    self.arrows -= 1
    return f'{self.arrows} remaining'

  def run(self):
    return 'ran really fast'


class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)


hb1 = HybridBorg('borgie', 50, 100)
hb1.shoot_arrows()
