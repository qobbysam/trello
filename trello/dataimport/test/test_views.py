from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import UserHandInput


class HomeRouteTest(TestCase):
    
    def test_home_url_location(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
    
    def test_home_url_name(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)

    def test_home_uses_correct_template(self):
        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'home.html')


class HandInputViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='2244kksl2')
        #test_user2 = User.objects.create_user(username='testuser2', password='2244kksl2')

        test_user1.save()
        #test_user2.save()

        test_input_1 = UserHandInput.objects.create(age=20, user=test_user1)

        test_input_1.save()

    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('handinput'))

        self.assertRedirects(response, '/accounts/login/?next=/imports/hand/')

    def test_logged_in_user_access(self):
        login = self.client.login(username='testuser1', password='2244kksl2')

        response = self.client.get(reverse('handinput'))

        #self.assertEqual(str(response.context['user'], 'testuser1'))
        self.assertRedirects(response, "/")
        self.assertEqual(response.status_code, 302)
        #self.assertTrue('session.input_obj' in response.context)
    
    def test_logged_in_post(self):

        login =self.client.login(username='testuser1', password='2244kksl2')

        data = {'age':'20'}

        response = self.client.post(reverse('handinput'), data)

        self.assertRedirects(response, "/")
        self.assertEqual(response.status_code, 302)

