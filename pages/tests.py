from django.test import TestCase
from django.urls import reverse


class PageViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_status_code(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_about_us_page_template(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Home")

    def test_about_us_page_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, "About Us")
