from django.db import models
from django.urls import reverse
import logging 

logger = logging.getLogger(__name__)
# Create your models here.
class Book(models.Model):
    
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse('book_detail', args=[str(self.id)])
        logger.error(f'{self.id}, {url}, \n')
        return url