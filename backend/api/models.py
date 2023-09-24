from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    title = models.CharField(max_length=256, default="No title")
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title
