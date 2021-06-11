
import random

# create a Product class with 5 fields

class Product:

    def __init__(self, name, price=10, weight=20,
                 flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        '''
        Calculates stealability based on price and weight, then
        returns a message telling how stealable the product is.
        '''
        self.stealability1 = self.price / self.weight
        if self.stealability1 < 0.5:
            return 'Not so stealable...'
        elif self.stealability1 < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        '''
        Calculates explosiveness based on flammability and weight,
        and then returns a message: if the product is less than 10
        returns "...fizzle.", if it is greater or equal to 10 but
        less than 50 returns "...boom!", and otherwise returns
         "...BABOOM!!"
        '''
        self.explosiveness = self.flammability * self.weight
        if self.explosiveness < 10:
            return '...fizzle'
        elif self.explosiveness < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, flammability)
        self.weight = weight

    def explode(self):
        '''
        Attempts to override parent method. It's a glove, and does
        not explode.
        '''
        return "It's a glove."

    def punch(self):
        '''
        Calculates hurtability based on weight, then
        returns a message telling how much it hurt.
        '''
        self.hurtability1 = self.price / self.weight
        if self.weight < 5:
            return 'That tickles'
        elif self.hurtability1 < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
        #return 'That tickles.'