from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs', validators=[FileExtensionValidator(['csv'])],\
        help_text='Допускаются только файлы формата .csv', blank=True, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}" 