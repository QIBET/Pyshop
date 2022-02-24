from django.test import TestCase
import unittest

from .models import Product, Offer

'''
Kindly check out the tests below if written correctly
'''
class ProductTestCase(unittest.TestCase):

    def Test_save_product():
        new_product = Product('name', 'price', 'stock', 'image_url')
        new_product.save_product()
