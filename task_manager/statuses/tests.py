from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status

User = get_user_model()


class StatusTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='Imya',
            last_name='Familiya',
            username='Test',
            password='12345'
        )
        self.status = Status.objects.create(name='TestStatus')

    def test_statuses_list(self):
        self.client.force_login(self.user)

        url = reverse('index_statuses')
        response = self.client.get(url)

        self.assertContains(response, 'TestStatus')

    def test_status_create(self):
        self.client.force_login(self.user)
        create_url = reverse('create_status')

        self.client.post(create_url,
            data={
                'name': 'NewStatus'
            })
        
        response = self.client.get(reverse('index_statuses'))

        self.assertContains(response, 'TestStatus')
        self.assertContains(response, 'NewStatus')

    def test_status_update(self):
        update_url = reverse('update_status', kwargs={'pk': self.status.id})
        list_url = reverse('index_statuses')
        self.client.force_login(self.user)

        self.client.post(update_url,
                         data={
                             'name': 'UpdatedStatus'
                            }
                        )
        
        response = self.client.get(list_url)

        self.assertContains(response, 'UpdatedStatus')
        self.assertNotContains(response, 'TestStatus')

    def test_status_delete(self):
        self.client.force_login(self.user)

        delete_url = reverse('delete_status', kwargs={'pk': self.status.id})
        list_url = reverse('index_statuses')
        
        response = self.client.get(list_url)
        self.assertContains(response, 'TestStatus')

        self.client.post(delete_url)

        response = self.client.get(list_url)
        self.assertNotContains(response, 'TestStatus')
