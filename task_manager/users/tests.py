
# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='Imya',
            last_name='Familiya',
            username='Test',
            password='12345'
        )

    def test_users_list(self):
        url = reverse('index_users')
        
        response = self.client.get(url)

        self.assertIn('users', response.context)
        self.assertContains(response, 'Test')

    def test_user_create(self):

        create_url = reverse('create_user')

        self.client.post(create_url,
            data={
                'first_name': 'NewImya',
                'last_name': 'Familiya',
                'username': 'NewTest',
                'password1': '12345',
                'password2': '12345'
            })
        
        response = self.client.get(reverse('index_users'))

        self.assertContains(response, 'NewTest')
        self.assertContains(response, 'NewImya')

    def test_user_update(self):
        update_url = reverse('update_user', kwargs={'pk': self.user.id})
        list_url = reverse('index_users')
        self.client.force_login(self.user)

        self.client.post(update_url,
                         data={
                             'first_name': 'Imya', 
                             'last_name': 'Familiya',
                             'username': 'Updated',
                             'password1': '123',
                             'password2': '123'
                            }
                        )
        
        response = self.client.get(list_url)

        self.assertContains(response, 'Updated')
        self.assertNotContains(response, 'Test')

    def test_user_delete(self):
        self.client.force_login(self.user)

        delete_url = reverse('delete_user', kwargs={'pk': self.user.id})
        list_url = reverse('index_users')
        
        response = self.client.get(list_url)
        self.assertContains(response, 'Test')

        self.client.post(delete_url)

        response = self.client.get(list_url)
        self.assertNotContains(response, 'Test')
