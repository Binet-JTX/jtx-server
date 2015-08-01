import datetime

from django.utils.timezone import utc
from rest_framework.test import APITestCase

from jtx_events.models import Event
from jtx_core.models.user import User

class EventTests(APITestCase):
    def setUp(self):
        self.create_data = {
            'title': 'Test', 
            'description': 'Description test',
            'begin_date': datetime.datetime(2015, 6, 15, 9, 30, 0, 0, tzinfo=utc),
            'end_date': datetime.datetime(2015, 8, 28, 17, 0, 0, 0, tzinfo=utc),
        }
        self.event, _ = Event.objects.get_or_create(title='', description='')

        self.user, _ = User.objects.get_or_create(email="bob@test.com")

    def test_get_event(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/events/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.event.title)

    def test_create_event(self):
        # Unauthenticated
        response = self.client.post('/events/', self.create_data)
        self.assertEqual(response.status_code, 403)

    def test_create_event(self):
        # Authenticated
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/events/', self.create_data)
        self.assertEqual(response.status_code, 201)
