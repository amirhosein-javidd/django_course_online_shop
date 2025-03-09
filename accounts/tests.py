from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserCreationFormTest(TestCase):
    def test_user_creation_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_creation_form_invalid(self):
        form_data = {'username': '', 'email': 'testuser@example.com', 'password1': 'password123', 'password2': 'password123'}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_creation_form_password_mismatch(self):
        form_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password1': 'password123', 'password2': 'password321'}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class CustomUserChangeFormTest(TestCase):
    def setUp(self):
        # ایجاد یک کاربر برای تست
        self.user = get_user_model().objects.create_user(username='testuser', email='testuser@example.com', password='password123')

    def test_user_change_form_valid(self):
        form_data = {'username': 'newuser', 'email': 'newuser@example.com'}
        form = CustomUserChangeForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_user_change_form_invalid(self):
        form_data = {'username': '', 'email': 'newuser@example.com'}
        form = CustomUserChangeForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())


class CustomUserAdminTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(username='admin', email='admin@example.com', password='password123')

    def test_custom_user_admin(self):
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('admin:accounts_customuser_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_custom_user_admin_add(self):
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('admin:accounts_customuser_add'))
        self.assertEqual(response.status_code, 200)

