from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import File
from .tasks import process_file


class FileAPITestCase(APITestCase):
    def test_upload_file(self):
        upload_file = open('test.txt', 'rb')
        response = self.client.post(reverse('upload_file'), {
                                    'file': upload_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(File.objects.filter(file='uploads/test.txt').exists())
        self.assertTrue(
            self.client.celery_app.tasks['process_file'].apply_async.called)
        upload_file.close()

    def test_list_files(self):
        File.objects.create(file='uploads/file1.txt', processed=True)
        File.objects.create(file='uploads/file2.txt', processed=False)
        response = self.client.get(reverse('file-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertTrue(response.data[0]['processed'])

        self.assertFalse(response.data[1]['processed'])


class CeleryTestCase(TestCase):
    def test_process_file_task(self):
        file = File.objects.create(file='uploads/test.txt')
        process_file(file.id)
        updated_file = File.objects.get(id=file.id)
        self.assertTrue(updated_file.processed)
