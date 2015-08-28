from django.test import TestCase
from models import Post

class PostTest(TestCase):
	def test_str(self):
		my_title = Post(title='This is a basic title for a basic test case')
		self.assertEquals(str(my_title), 'This is a basic title for a basic test case',)

# Create your tests here.
