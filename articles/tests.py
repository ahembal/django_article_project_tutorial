from django.http import response
from django.test import TestCase  # we are going to test our database
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Article

class TestSite(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='sampleuser',
            email='sample@aol.com',
            password = 'password',
            )

        self.article = Article.objects.create(
            title='Axehandle Hounds Ravage Minnesota',
            text='Test article test nothing important what it is...',
            author= self.user,
            )
        
    def test_article_title(self):  # you can name this anything you want
        article = Article(title='Axehandle Hounds Ravage Minnesota')
        self.assertEqual(str(article), article.title)
        
    def test_setting_all(self):
        self.assertEqual(f'{self.article.title}', 'Axehandle Hounds Ravage Minnesota')
        self.assertEqual(f'{self.article.author}', 'sampleuser')
        self.assertEqual(f'{self.article.text}', 'Test article test nothing important what it is...')
        
    def test_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)   #home page response checked
        self.assertContains(response, 'Axehandle Hounds Ravage Minnesota')    # checked if response contains this text
        self.assertTemplateUsed(response, 'home.html')
        
    def test_article_detail_view(self):
        response = self.client.get('/article/1/')  # '/article/1' gives 301 response which means moved permanently
        bad_response = self.client.get('/article/200/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bad_response.status_code, 404)
        self.assertContains(response, 'Axehandle Hounds Ravage Minnesota')
        self.assertTemplateUsed(response, 'article_detail.html')

    def test_article_creation(self):
        response = self.client.post(reverse('new_article'),{
            'title': 'Sample Title',
            'text' : 'Sample Text',
            'author' : self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Title')
        self.assertContains(response, "Sample Text")

    def test_article_update(self):
        response = self.client.post(reverse('article_edit', args='1'),{
            'title' : 'New Title',
            'text' : 'New Text',
        })
        self.assertEqual(response.status_code, 302)

    def test_article_delete(self):
        response = self.client.get(reverse('article_delete', args='1'))
        self.assertEqual(response.status_code, 200)  # this response meaning that it no longer exists