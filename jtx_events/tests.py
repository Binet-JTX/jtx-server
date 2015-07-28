import datetime

from django.utils.timezone import utc
from rest_framework.test import APITestCase

from jtx_events.models import Event

class EventTests(APITestCase):
    def setUp(self):
        self.create_data = {
            'title': 'Test', 
            'description': 'Description test',
            'begin_date': datetime.datetime(2015, 6, 15, 9, 30, 0, 0, tzinfo=utc),
            'end_date': datetime.datetime(2015, 8, 28, 17, 0, 0, 0, tzinfo=utc),
        }
        self.event, _ = Event.objects.get_or_create(title='', description='')

    # def test_get_event(self):
    #     response = self.client.get('/events/')
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['title'], self.event.title)

    def test_create_event(self):
        # Unauthenticated
        response = self.client.post('/events/', self.create_data)
        self.assertEqual(response.status_code, 401)
