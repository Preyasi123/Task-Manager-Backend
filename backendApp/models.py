from django.db import models

# Create your models here.
class Todo(models.Model):
    Id=  models.AutoField(primary_key=True)
    Title= models.CharField(max_length=255)
    Description=models.TextField(max_length=100)
    Status = models.BooleanField(default=False, verbose_name="Completed")
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title