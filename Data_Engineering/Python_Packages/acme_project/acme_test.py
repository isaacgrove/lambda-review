import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability_and_explode(self):
        """Test that a new object's stealability() and
        explode() methods function as they should."""
        prod = Product('Test Product', price=500, flammability=100.0)
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Making sure the report works right"""
    def test_default_num_products(self):
        """Checks that product list length is actually 30."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test default product list contains all valid names.
        First assertion is that the first word is in ADJECTIVE list.
        Second assertion is that second word is in NOUN list.
        Third assertion is that there is a space in the product name."""
        for prod in generate_products():
            split_name = prod.name.split()
            self.assertIn(split_name[0], ADJECTIVES)
            self.assertIn(split_name[1], NOUNS)
            self.assertIn(' ', prod.name)

if __name__ == '__main__':
    unittest.main()
