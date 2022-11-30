from django.db import models


class GenericFileUpload(models.Model):
    file_upload = models.FileField()
    created_at = models.DataTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.file_upload}"
