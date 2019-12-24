from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    
    def test_create_user_with_email(self):
        email = 'test@google.com'
        password = "123"
        user = get_user_model().objects.create_user(
            email = email, 
            password = password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        email = 'test@google.COM'
        user = get_user_model().objects.create_user(
           email, 'test123'
        )
        
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    def test_create_new_super_user(self):
        email = 'testadmin@google.com'
        password = "123"
        user = get_user_model().objects.create_user(
            email = email, 
            password = password
        )

        user.is_superuser = True
        user.is_staff = True
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
