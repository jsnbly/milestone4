from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    content = models.TextField()
    contact_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.title