from django.db import models

# Create your models here.
class Gallery(models.Model):
    description=models.CharField(default='xie jian jie',max_length=100)
    image=models.ImageField(default='screen.jpg',upload_to='images/')
    title=models.CharField(default='title',max_length=10)
    def __str__(self):
        return self.title
