from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

User = get_user_model()


class TasksTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='Imya',
            last_name='Familiya',
            username='Test',
            password='12345'
        )
        self.status = Status.objects.create(name='TestStatus')

        self.task = Task.objects.create(
            name='TestTask',
            description='TestDescription',
            author=self.user,
            status=self.status
        )

    def test_statuses_list(self):
        self.client.force_login(self.user)

        url = reverse('index_tasks')
        response = self.client.get(url)

        self.assertContains(response, 'TestTask')
        self.assertContains(response, 'TestStatus')
        self.assertContains(response, 'Imya Familiya')

    def test_task_create(self):
        self.client.force_login(self.user)
        create_url = reverse('create_task')

        self.client.post(create_url,
            data={
                'name': 'NewTask',
                'status': self.status.id,
                'executor': ''
            }
        )
        
        response = self.client.get(reverse('index_tasks'))

        self.assertContains(response, 'NewTask')

    def test_status_update(self):
        update_url = reverse('update_task', kwargs={'pk': self.task.id})
        list_url = reverse('index_tasks')
        self.client.force_login(self.user)

        self.client.post(
            update_url,
            data={
                'name': 'UpdatedTask',
                'status': Status.objects.create(name='NewStatus').id,
                'executor': self.user.id
            }
        )
        
        response = self.client.get(list_url)

        self.assertContains(response, 'UpdatedTask')
        self.assertNotContains(response, 'TestTask')
        self.assertContains(response, 'NewStatus')
        self.assertContains(response, 'Imya Familiya')

    def test_status_delete(self):
        self.client.force_login(self.user)

        delete_url = reverse('delete_task', kwargs={'pk': self.task.id})
        list_url = reverse('index_tasks')
        
        response = self.client.get(list_url)
        self.assertContains(response, 'TestTask')

        self.client.post(delete_url)

        response = self.client.get(list_url)
        self.assertNotContains(response, 'TestTask')