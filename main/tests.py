from django.test import TestCase
from django.test import TestCase, Client
from main.models import Product

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="ice americano", amount="0")
        Product.objects.create(name="caffe latte", amount="10")

    def test_products_has_stock(self):
        # check if product has stocks
        caffe_latte = Product.objects.get(name="caffe latte")
        self.assertEqual(caffe_latte.check_stock(), 'Stock of caffe latte is 10!')

    def test_products_has_no_stock(self):
        ice_americano = Product.objects.get(name="ice americano")
        self.assertEqual(ice_americano.check_stock(), 'Stock of ice americano is not available.')