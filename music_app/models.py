from django.db import models

# Create your models here.
class category(models.Model):
    name=models.TextField()

class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    paginate_by = 2

    def __str__(self):
        return self.title
