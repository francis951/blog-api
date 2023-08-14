from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user_one = User.objects.create_user(username = "admin2", password = "admin2")
        test_user_one.save()
        # Create a blog post
        test_post = Post.objects.create(author = test_user_one, title = 'Blog goes here ...', body = 'Body contents here ...')
        test_post.save()
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'admin2')
        self.assertEqual(title, 'Blog goes here ...')
        self.assertEqual(body, 'Body contents here ...')       