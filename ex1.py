class Animal:
    def __init__(self, name, age, food, hunger, weight, height):
        self.name = name
        self.age = age
        self.food = food
        self.hunger = hunger
        self.weight = weight
        self.height = height

    def eat(self):
        if (self.hunger < 10):
            self.hunger += 1
        else: 
            print("Сытый")
    
    def make_move(self):
        if (self.hunger > 0):
            self.hunger -= 1
        else:
            print("Голодный")

class Mammal(Animal):
    def __init__(self, name, age, food, hunger, weight, height, is_fluffy, gender):
        super().__init__(name, age, food, hunger, weight, height)
        self.is_fluffy = is_fluffy
        self.gender = gender

    def make_noise(self):
        print("*Издает какой-то звук*")

class Human(Mammal):
    def __init__(self, name, age, food, hunger, weight, height, is_fluffy, gender, intelligence):
        super().__init__(name, age, food, hunger, weight, height, is_fluffy, gender)
        self.intelligence = intelligence

    def say(self):
        print(f'Привет, меня зовут {self.name}!')

class Cat(Mammal):
    def __init__(self, name, age, food, hunger, weight, height, is_fluffy, gender, hearing):
        super().__init__(name, age, food, hunger, weight, height, is_fluffy, gender)
        self.hearing = hearing

    def make_noise(self):
        print("Мяу")

class Dog(Mammal):
    def __init__(self, name, age, food, hunger, weight, height, is_fluffy, gender, scent):
        super().__init__(name, age, food, hunger, weight, height, is_fluffy, gender)
        self.scent = scent

    def make_noise(self):
        print("Гав")
