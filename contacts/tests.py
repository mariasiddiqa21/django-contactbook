from django.test import TestCase
from django.urls import reverse
from .models import Contact
from django.core.exceptions import ValidationError



class ContactModelTest(TestCase):

    def test_valid_contact(self):
        """Valid contact should pass full_clean without errors"""
        c = Contact(name="Maria", phone="0300123456", email="maria@example.com")
        try:
            c.full_clean()  # runs model validators
        except ValidationError:
            self.fail("Valid contact raised ValidationError")

    def test_invalid_phone(self):
        """Phone number not matching regex should raise ValidationError"""
        c = Contact(name="Test", phone="12345", email="test@example.com")
        with self.assertRaises(ValidationError):
            c.full_clean()

    def test_invalid_email(self):
        """Invalid email should raise ValidationError"""
        c = Contact(name="Test", phone="0300123456", email="invalidemail")
        with self.assertRaises(ValidationError):
            c.full_clean()

    def test_invalid_name(self):
        """Name with numbers or special characters should raise ValidationError"""
        c = Contact(name="Maria123", phone="0300123456", email="maria@example.com")
        with self.assertRaises(ValidationError):
            c.full_clean()



class ContactViewTest(TestCase):

    def setUp(self):
        """Create some sample contacts"""
        self.contact1 = Contact.objects.create(
            name="Maria",
            phone="0300123456",
            email="maria@example.com"
        )
        self.contact2 = Contact.objects.create(
            name="Ali",
            phone="0300987654",
            email="ali@example.com"
        )

    
    def test_contact_list_view_status_and_template(self):
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_list.html')
        self.assertContains(response, "Maria")
        self.assertContains(response, "Ali")

    
    def test_add_contact_view(self):
        data = {
            "name": "TestUser",
            "phone": "0300111222",
            "email": "testuser@example.com"
        }
        response = self.client.post(reverse('add_contact'), data)
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(Contact.objects.count(), 3)

    
    def test_update_contact_view(self):
        data = {
            "name": "Maria Updated",
            "phone": "0300999888",
            "email": "maria_updated@example.com"
        }
        response = self.client.post(reverse('edit', args=[self.contact1.id]), data)
        self.assertEqual(response.status_code, 302)

        self.contact1.refresh_from_db()
        self.assertEqual(self.contact1.name, "Maria Updated")
        self.assertEqual(self.contact1.phone, "0300999888")
        
        self.assertEqual(self.contact1.email, "maria_updated@example.com")

    
    def test_delete_contact_view(self):
        response = self.client.get(reverse('delete', args=[self.contact2.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contact.objects.filter(id=self.contact2.id).exists())

    
    def test_search_functionality_database(self):
        """Since JS handles frontend search, test DB filtering instead"""
        query = "Maria"
        results = Contact.objects.filter(
            name__icontains=query
        )
        self.assertIn(self.contact1, results)
        self.assertNotIn(self.contact2, results)

        query = "Ali"
        results = Contact.objects.filter(
            name__icontains=query
        )
        self.assertIn(self.contact2, results)
        self.assertNotIn(self.contact1, results)
