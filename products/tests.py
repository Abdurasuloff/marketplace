from django.test import TestCase
from users.models import CustomUser
from .models import Category, Product

# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        user = CustomUser.objects.create(username='akbarjon', email='aa@aa.aa')
        user.set_password('my_pass')
        user.save()
        self.client.login(username='akbarjon', password='my_pass')
    
    def test_product_created(self):
        Category.objects.create(name='cat')
        response = self.client.post(
            '/products/new',
            data={
                'title':'my title',
                'description':'pr desc',
                'price':123,
                'category':'1',
                'address':'pr address',
                'phone_number':'+998903693',
                'tg_username':'user',
            }
        )
        product = Product.objects.get(id=1)
        self.assertEqual(product.title, 'my title')
        self.assertEqual(product.description, 'pr desc')    
        self.assertEqual(product.price, 123)    
        self.assertEqual(product.address, 'pr address')    
        self.assertEqual(product.category.id, 1)    
        
        second_response = self.client.post(
            '/products/1/update',
            data={
                'title':'my titles',
                'description':'pr descr',
                'price':1234,
                'category':'1',
                'address':'pr address',
                'phone_number':'+998903693',
                'tg_username':'users',
            }
        )
        product = Product.objects.get(id=1)
        self.assertEqual(product.title, 'my titles')
        self.assertNotEqual(product.title, 'my title')
        self.assertEqual(product.description, 'pr descr')    
        self.assertEqual(product.price, 1234)    
        self.assertEqual(product.address, 'pr address')    
        self.assertEqual(product.category.id, 1) 
        
        third_response = self.client.post(
            '/products/1/delete',
        )
        self.assertEqual(Product.objects.all().count(), 0)
