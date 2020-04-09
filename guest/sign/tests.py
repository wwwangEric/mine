from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User

# Create your tests here.
class IndexPageTest(TestCase):
	def test_index_page_renders_index_templates(self):

		response = self.client.get('/index/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'index.html')

class LoginActionTest(TestCase):

	def setUp(self):
		User.objects.create_user('admin','admin@mail.com','admin123456')

	def test_add_admin(self):
		user = User.objects.get(username = 'admin')
		self.assertEqual(user.username,'admin')
		self.assertEqual(user.email,'admin@mail.com')

	def test_login_action_username_password_null(self):
		test_date = {'username':'','password':''}
		response = self.client.post('/login_action/',data=test_date)
		self.assertEqual(response.status_code,200)
		self.assertIn(b'username or password error! Please check~',response.content)

	def test_login_action_username_password_error(self):
		test_date = {'username':'root','password':'root1234'}
		response = self.client.post('/login_action/',test_date)
		self.assertEqual(response.status_code,200)
		self.assertIn(b'username or password error! Please check~',response.content)

	def test_login_action_success(self):
		test_date = {'usernmae':'admin','password':'admin123456'}
		response = self.client.post('login_action',test_date)
		self.assertEqual(response.status_code,302)