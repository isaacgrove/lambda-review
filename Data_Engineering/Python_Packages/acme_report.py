import random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    ''' Generates a list of 30 products. '''
    products = []

    for number in range(1, num_products + 1):

        f_name = str(random.sample(ADJECTIVES, 1)).lstrip("['").rstrip("']")
        l_name = str(random.sample(NOUNS, 1)).lstrip("['").rstrip("']")
        name = f_name + ' ' + l_name
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = (random.randint(1, 26) - 1) / 10

        product = Product(name, price, weight, flammability)

        products.append(product)
    return products


def inventory_report(products):
    ''' Prints a nice inventory report. '''
    names_list = []
    price_list = []
    weight_list = []
    flammability_list = []

    for product in products:
        names_list.append(product.name)
        price_list.append(product.price)
        weight_list.append(product.weight)
        flammability_list.append(product.flammability)

    num_unique_names = len(set(names_list))
    avg_price = sum(price_list) / len(price_list)
    avg_weight = sum(weight_list) / len(weight_list)
    avg_flammability = sum(flammability_list) / len(flammability_list)

    output = print('ACME CORP OFFICIAL INVENTORY REPORT\n',
                   'Unique product names: ', num_unique_names,
                   '\nAverage price: ',
                   avg_price, '\nAverage weight: ',
                   avg_weight, '\nAverage Flammability: ',
                   avg_flammability)

    return output

if __name__ == '__main__':
    inventory_report(generate_products())
