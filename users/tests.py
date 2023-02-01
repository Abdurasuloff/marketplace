from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user
# Create your tests here.

class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data = {
                'first_name':'Akbarjon',
                'username':'akbarjon',
                'email':'aa@aa.aa',
                'password1':'chalamulla',
                'password2':'chalamulla',
            }
        )
        user=CustomUser.objects.get(username='akbarjon')
        self.assertEqual(user.first_name, 'Akbarjon')
        self.assertEqual(user.email, 'aa@aa.aa')
        self.assertTrue(user.check_password('chalamulla'))
    
        second_response = self.client.get("/users/profile/akbarjon") 
        self.assertEqual(second_response.status_code, 200)   
        
        #login
        self.client.login(username='akbarjon', password='chalamulla')
        
        third_response = self.client.post(
            reverse('users:update'),
            data={
                'username':'akbarjon2',
                'first_name':'Akbarjon2',
                'last_name':'Abdurasulov',
                'email':'aaa@aaa.aaa',
                'phone_number':'+998902323',
                'tg_username':'username',
            }
        )
        user = get_user(self.client)  
        print(user.is_authenticated)
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.phone_number, '+998902323')
        self.assertEqual(user.first_name, 'Akbarjon2')
        self.assertNotEqual(user.first_name, 'Akbarjon')
        
        