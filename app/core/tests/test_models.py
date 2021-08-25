from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
  def test_create_user_with_email_successful(self):
    """Test creating a new user with an email is successful"""
    email = 'testmail122402@gmail.com'
    password = 'Xuanvan2412'
    user = get_user_model().objects.create_user(
      email = email,
      password = password,
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    """Test the email for a new user is normalized"""
    email = 'testmail122402@GMAIL.COM'
    user = get_user_model().objects.create_user(email, 'Xuanvan2412')

    self.assertEqual(user.email, email.lower())

  def test_new_user_invalid_email(self):
    """Test creating user with no email raises error"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'Xuanvan2412')

  def test_create_new_superuser(self):
    """Test creating a new superuser"""
    user = get_user_model().objects.create_superuser(
      'testmail122402@gmail.com',
      'Xuanvan2412'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)





