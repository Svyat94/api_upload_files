from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .serializers import UserSerializer, FileSerializer
from .models import File
from .tasks import process_file


@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # Сохраняем пользователя, который загрузил файл
            file_serializer.save(user=request.user)
            file_id = file_serializer.data['id']
            # Запускаем Celery задачу для обработки файла
            process_file.delay(file_id)
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
