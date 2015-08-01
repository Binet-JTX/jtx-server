from rest_framework.test import APITestCase
from jtx_core.models.user import User, UserSerializer

def reload(obj):
    return obj.__class__.objects.get(pk=obj.pk)


class BackendTests(APITestCase):
    @classmethod
    def setUpTestData(self):
        super(BackendTests, self).setUpTestData()
        User.objects.create_user("test@test.com", "test")


    def test_login(self):
        data = {'email': 'test@test.com', 'password': 'test'}
        response = self.client.post('/api-token-auth/', data, format='json')

        self.assertEqual(response.status_code, 200)

        token = response.data["token"]
        auth = 'JWT {0}'.format(token)
        response = self.client.get('/users/me/', HTTP_AUTHORIZATION=auth, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], "test@test.com")

    def test_login_wrong_password(self):
        data = {'email': 'test@test.com', 'password': 'sdgez'}
        response = self.client.post('/api-token-auth/', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_login_wrong_user(self):
        data = {'username': 'not_admin', 'password': 'test'}
        response = self.client.post('/api-token-auth/', data, format='json')

        self.assertEqual(response.status_code, 400)


    def test_add_superuser(self):
        u = User.objects.create_superuser("su", "su")
        self.assertTrue(u.is_superuser)
        self.assertTrue(u.is_staff)


class UserTests(APITestCase):
    @classmethod
    def setUpTestData(self):
        super(UserTests, self).setUpTestData()
        self.manager, _ = User.objects.get_or_create(email="manager@test.com")
        self.manager.is_staff = True
        self.manager.save()

        self.user, _ = User.objects.get_or_create(email="bob@test.com")
        self.user.set_password("password")
        self.user.save()

        serializer = UserSerializer(self.user)
        self.data = serializer.data
        self.user_url = '/users/%d/' % self.user.id

    def setUp(self):
        self.data['email'] = "bob@test.com"
        self.user.email = "bob@test.com"
        self.user.save()

    def test_get_user_not_authed(self):
        # Not authenticated
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, 403)

    def test_get_user_authed(self):
        # Authenticated
        self.client.force_authenticate(user=User())
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], self.data['email'])

