from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vendor, HistoricalPerformance
from datetime import datetime

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name="Test Vendor", contact_details="123-456-7890", address="123 Main St")
        self.historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            date=datetime.now(),
            on_time_delivery_rate=0.85,
            quality_rating_avg=4.5,
            average_response_time=2.5,
            fulfillment_rate=0.95
        )

    def test_vendor_list(self):
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vendor(self):
        data = {
            'name': 'New Vendor',
            'contact_details': '123-456-7890',
            'address': '123 Main St'
        }
        response = self.client.post('/api/vendors/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_vendor(self):
        response = self.client.get(f'/api/vendors/{self.vendor.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_vendor(self):
        data = {
            'name': 'Updated Vendor Name',
            'contact_details': '123-456-7890',
            'address': '123 Main St'
        }
        response = self.client.put(f'/api/vendors/{self.vendor.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vendor(self):
        response = self.client.delete(f'/api/vendors/{self.vendor.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_historical_performance_retrieve(self):
        response = self.client.get(f'/api/vendors/{self.vendor.id}/performance/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

