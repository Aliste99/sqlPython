class Cat:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.health = 10
        self.mood = 10
        self.hunger = 10
        self.alive = True
        
    def feed(self):
        if self.alive:
            if self.hunger > 8:
                self.health -= 1
            self.hunger += 1
            self.mood = self.mood + 10/self.mood
        else:
            print("Your " + self.name + "is dead((9(")
        if self.hunger <= 0 or self.health <= 0 or self.mood <= 0:
            dead()
            
    def jump(self):
        if self.alive:
            if self.mood < 3:
                print("I'm sad. I don't want to do this")
            elif self.hunger < 3:
                print("Give me some food. I'll do this after that")
            elif self.health < 3:
                print("I feel bad")
            else:
                self.health -= 1
                self.hunger -= 1
                self.mood -= 1
                print("__/----\__/----\__")
                print("P.S. it's a jump :3")
        else:
            print("Your " + self.name + " is dead((9(")
        if self.hunger <= 0 or self.health <= 0 or self.mood <= 0:
            dead()
            
    def check(self):
        if self.alive:
            print(self.health)
            print(self.mood)
            print(self.hunger)
        else:
            print("Your " + self.name + "is dead((9(")
        if self.hunger <= 0 or self.health <= 0 or self.mood <= 0:
            dead()
        
    def dead(self):
        self.alive = False
            