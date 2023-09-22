from celery import shared_task
from .models import File


@shared_task
def process_file(file_id):
    try:
        file = File.objects.get(pk=file_id)
        # Здесь выполняйте обработку файла
        # Например, обработка изображений, текстовых файлов и т.д.
        # Установите file.processed = True после обработки
        file.processed = True
        file.save()
    except File.DoesNotExist:
        pass
