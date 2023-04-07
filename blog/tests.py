from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post


class BlogPostTest(TestCase):
    # def setUp(self):
    #     self.user1 = User.objects.create(username='user 1')
    #     self.post1 = Post.objects.create(
    #         title='post 1',
    #         text='text 1',
    #         status=Post.STATUS_CHOICES[0][0],  # 'pub'
    #         author=self.user1
    #     )
    #     self.post2 = Post.objects.create(
    #         title='post 2',
    #         text='text 2',
    #         status=Post.STATUS_CHOICES[1][0],  # 'drf'
    #         author=self.user1
    #     )

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(username='user 1')
        cls.post1 = Post.objects.create(
            title='post 1',
            text='text 1',
            status=Post.STATUS_CHOICES[0][0],  # 'pub'
            author=cls.user1
        )
        cls.post2 = Post.objects.create(
            title='post 2',
            text='text 2',
            status=Post.STATUS_CHOICES[1][0],  # 'drf'
            author=cls.user1
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'post 1')
        self.assertEqual(self.post1.text, 'text 1')
        self.assertEqual(self.post1.status, 'pub')
        self.assertEqual(self.post1.author, self.user1)

    def test_posts_list_by_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_posts_list_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_on_blog_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.author)

    def test_post_detail_by_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.author)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[10000000]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'some title',
            'text': 'this is some text',
            'status': 'pub',
            'author': self.user1.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().text, 'this is some text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'post 2 updated',
            'text': 'text 2 updated',
            'status': 'pub',
            'author': self.user1.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'post 2 updated')
        self.assertEqual(Post.objects.last().text, 'text 2 updated')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
