from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class ListTests(TestCase):
  def test_snack_list_status_code(self):
    url = reverse("snacks_list")
    response=self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_home_page_template(self):
    url = reverse("snacks_list")
    response=self.client.get(url)
    self.assertTemplateUsed(response,"snacks_list.html")  