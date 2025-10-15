from django.db import models
from django.contrib.auth.models import User

def client_file_path(instance, filename):
    # Example path: uploads/client_5/user_2/invoice.pdf
    return f"uploads/client_{instance.client_id}/user_{instance.user.id}/{filename}"

class UploadedFile(models.Model):
    FILE_TYPES = (
        ('pdf', 'PDF'),
        ('csv', 'CSV'),
        ('xls', 'Excel'),
        ('unknown', 'Unknown'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_id = models.PositiveIntegerField()  # Adapt later to your Client model
    file = models.FileField(upload_to=client_file_path)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, default='unknown')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.file_type})"
