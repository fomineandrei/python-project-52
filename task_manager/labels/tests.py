from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label

User = get_user_model()


class LabelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='Imya',
            last_name='Familiya',
            username='Test',
            password='12345'
        )
        self.label = Label.objects.create(name='TestLabel')

    def test_labels_list(self):
        self.client.force_login(self.user)

        url = reverse('index_labels')
        response = self.client.get(url)

        self.assertContains(response, 'TestLabel')

    def test_label_create(self):
        self.client.force_login(self.user)
        create_url = reverse('create_label')

        self.client.post(create_url,
            data={
                'name': 'NewLabel'
            })
        
        response = self.client.get(reverse('index_labels'))

        self.assertContains(response, 'TestLabel')
        self.assertContains(response, 'NewLabel')

    def test_label_update(self):
        update_url = reverse('update_label', kwargs={'pk': self.label.id})
        list_url = reverse('index_labels')
        self.client.force_login(self.user)

        self.client.post(update_url,
                         data={
                             'name': 'UpdatedLabel'
                            }
                        )
        
        response = self.client.get(list_url)

        self.assertContains(response, 'UpdatedLabel')
        self.assertNotContains(response, 'TestLabel')

    def test_label_delete(self):
        self.client.force_login(self.user)

        delete_url = reverse('delete_label', kwargs={'pk': self.label.id})
        list_url = reverse('index_labels')
        
        response = self.client.get(list_url)
        self.assertContains(response, 'TestLabel')

        self.client.post(delete_url)

        response = self.client.get(list_url)
        self.assertNotContains(response, 'TestLabel')