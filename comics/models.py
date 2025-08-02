from django.db import models

# Create your models here.
class ComicGenre(models.Model):
    gname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.gname

class ComicDetails(models.Model):
    cname = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    totalEpisode = models.IntegerField()
    totalView = models.IntegerField()
    totalLike = models.IntegerField()
    image = models.ImageField(upload_to='comics/',blank=True,null=True)

    gname = models.ForeignKey(ComicGenre,on_delete=models.CASCADE)


    def __str__(self):
        return self.cname

