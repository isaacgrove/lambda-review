# Test from part 1

from acme import Product

prod = Product('A Cool Toy')
print(prod.name)
print(prod.price)
print(prod.weight)
print(prod.flammability)
print(prod.identifier)

print(prod.stealability())
print(prod.explode())

from acme import BoxingGlove
glove = BoxingGlove('Punchy the Third')
print(glove.price)
#10
print(glove.weight)
#10
print(glove.punch())
# 'Hey that hurt!'
print(glove.explode())
# "...it's a glove."