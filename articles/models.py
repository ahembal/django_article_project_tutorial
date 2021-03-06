from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(         #Unique identifier for our authors
        'auth.User',                    #This will handle authentication
        on_delete = models.CASCADE,     #If this object deleted, than delete all references
        default=1,                      #Because We have already article inside of it, main superuser
        )       
    photo = models.ImageField(upload_to="galery", default='drop-bear.jpg')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])  # This is going to return created page back after save