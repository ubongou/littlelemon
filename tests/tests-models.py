from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers  import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="Cake", price=90, inventory=90)
        item2 = Menu.objects.create(title="Yoghurt", price=70, inventory=110)

    def test_getall(self):
        response = self.client.get()
        menus = Menu.objects.all()
        serializer = MenuSerializer
        self.assertEqual(response.data, serializer.data)        
