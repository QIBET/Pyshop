from django.test import TestCase
from django.test import TestCase

from .models import Product, Offer

'''
Kindly check out the tests below if written correctly
'''
class ProductTestCase(TestCase):
    def setUp(self):
        '''
        test instance of a product
        '''
        self.new_product = Product(name ='melons', price = '1.35', stock = '5')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_product, Product))

    def test_save_product_method(self):
        self.new_product.save_product()
        products = Product.objects.all()
        self.assertTrue(len(products) > 0 )


       
