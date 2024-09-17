import numpy

#una semplicissima implementazione di varie cose viste (ereditarietà, composizione, classi, metodi) ispirata ad un videogioco

# classe gioco generica per gestire eventi 
class game: 
    def __init__(self):
        self.monsters = []
       
   

    def add_monster(self, monster):
        self.monsters.append(monster)

    # metodo fasullo che controlla se il colpo è andato a segno
    def check_collision(self):
        return (True, self.monsters[0])   

# classe astratta utile per essere estesa (ereditarietà)
class game_actor:
    def __init__(self, position, stats, game : game):
        self.position = position
        self.stats = stats
        self.game = game

# nemico
class monster(game_actor):
    def __init__(self, position, stats, ggame = None):
         super().__init__(position, stats, ggame)
         self.hostility = True
    def get_hit(self, d):
            self.stats["hp"] -= d

# classe arma utilizzabile da tutti (composizione)
class weapon:
    def __init__(self,stats):
       self.stats = stats

# classe personaggio
class main_character(game_actor):
        def __init__(self, position, stats, name, pg_class, game:game):
             super().__init__(position, stats, game)
             self.name = name
             self.pg_class = pg_class
             self.weapon = weapon({"name": "i pugni", "damage": 2, "speed": 1})

        def getWeapon(self, weapon: weapon):
             self.weapon = weapon
        
        def attack(self):
            
            collision, target = self.game.check_collision()
          
            if  collision: 
                damage = (1+(self.stats["strength"]/100)) * self.weapon.stats["damage"]
                target.get_hit(damage)
                print(self.name+" ha colpito "+target.stats["name"]+" con "+self.weapon.stats["name"]+", causando "+str(damage)+" danni!")



mygame = game()
orco = monster({"x": 1, "y": 0}, stats= {"name": "Grishnak la belva", "hp": 80, "damage": 10})
goblin = monster({"name": "Urkhul il Brutto", "x": 0, "y": 1}, stats={"name": "Urkhul il brutto","hp": 50, "damage": 3})
mygame.add_monster(orco)
mygame.add_monster(goblin)


warrior = main_character(
    {"x": 0, "y":0}, 
    {"hp": 150, "strength": 20}, 
    "Zyzz", 
    "Warrior", 
    mygame)

warrior.attack()
print(mygame.monsters[0].stats["hp"])
ascia = weapon({"name": "Ascia Bipenne", "damage": 30, "speed": 0.7})
warrior.getWeapon(ascia)
warrior.attack()
print(mygame.monsters[0].stats["hp"])


