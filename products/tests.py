from django.test import TestCase
from django.test import TestCase

from .models import Product, Offer,Customer

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

class OfferTestCase(TestCase):
    def setUp(self):
        self.new_offer = Offer(code = 'GJKHGNKNMMKLLNG', description = 'offer for frequent purchases', discount = '10.34')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_offer, Offer))

    def test_save_offer(self):
        self.new_offer.save_offer()
        offers = Offer.objects.all()
        self.assertTrue(len(offers) > 0)
       

class CustomerTestCase(TestCase):
    def setUp(self):
        self.new_customer = Customer(customer_name = 'Lorraine', location = 'Nairobi')

    def test_instance(self):
        self.assertTrue(self.new_customer, Customer)

    def test_save_customer(self):
        self.new_customer.save_customer()
        customers = Customer.objects.all()
        self.assertTrue(len(customers) > 0)

