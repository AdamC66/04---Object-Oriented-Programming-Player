# Create a class called Player.
# Every player should have three attributes: gold_coins, health_points, and lives.
# lives should start at 5.
# gold_coins should start at 0.
# health_points should start at 10.
# Define an __str__() instance method.
# Your class should have an instance method called level_up that increases lives by one.
# Your class should have an instance method called collect_treasure that increases gold_coins by one. 
# If gold_coins is a multiple of ten (eg, 10, 20, 30, and so on) then the collect_treasure method should run the level_up method.

# Your class should have an instance method called do_battle that accepts one damage argument and subtracts it from the player's health_points. 
# If health_points falls below one, subtract one from lives and reset health_points to ten. If you have run out of lives, 
# this method should run another method called restart (see below).
# The restart instance method should set all attributes back to their starting values (5, 0, and 10).

class Player:
    def __init__(self, lives=5, gold_coins=0, health_points=10):
        self.lives = lives
        self.gold_coins = gold_coins
        self.health_points = health_points
    def __str__(self):
        return f'Player has {self.lives} lives remaining, {self.gold_coins} gold and {self.health_points} health'
    def level_up(self):
        self.lives +=1
    def collect_treasure(self):
        self.gold_coins +=1
        if self.gold_coins % 10 == 0:
            self.level_up()
    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points <=0:
            self.health_points = 10
            self.lives -= 1
            if self.lives <= 0:
                print("YOU DIED")
                self.restart()
    def restart(self):
        self.lives = 5
        self.gold_coins = 0
        self.health_points =10

player1 = Player()
print(player1)
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
print(player1)
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
print(player1)

player1.do_battle(10)
print(player1)

player1.do_battle(10)
player1.do_battle(10)
player1.do_battle(10)
player1.do_battle(10)
print(player1)

player1.do_battle(10)
print(player1)
