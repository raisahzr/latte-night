from django.test import TestCase
from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Ice Americano", amount="0", price=15000, category="coffee", coffee_bean="Arabica")
        Item.objects.create(name="Caffe Latte", amount="10", price=25000, category="coffee", coffee_bean = "Robusta")
        Item.objects.create(name="Hibiscus Ice Tea", amount="5", price=20000, category="non-coffee", coffee_bean = "NONE")

    def test_products_has_stock(self):
        # check if product has stocks
        caffe_latte = Item.objects.get(name="Caffe Latte")
        self.assertEqual(caffe_latte.check_stock(), 'Stock of Caffe Latte is 10!')

    def test_products_has_no_stock(self):
        # check if product has no stocks
        ice_americano = Item.objects.get(name="Ice Americano")
        self.assertEqual(ice_americano.check_stock(), 'Stock of Ice Americano is not available.')

    def test_checkout(self):
        # checkout message
        ice_americano = Item.objects.get(name="Ice Americano")
        hibiscus = Item.objects.get(name="Hibiscus Ice Tea")
        self.assertEqual(ice_americano.checkout(), 'Your order is Ice Americano with Arabica coffee in total Rp15000.')
        self.assertEqual(hibiscus.checkout(), 'Your order is Hibiscus Ice Tea in total Rp20000.')