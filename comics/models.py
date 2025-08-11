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
    poster_image = models.ImageField(upload_to='comics_poster/',blank=True,null=True)
    

    gname = models.ForeignKey(ComicGenre,on_delete=models.CASCADE)


    def __str__(self):
        return self.cname



class ComidEpisodes(models.Model):
    EpisodeNo = models.IntegerField()
    EpisodeName = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='comics_chapters/',blank=True,null=True)

    totalEpisode = models.ForeignKey(ComicDetails,on_delete=models.CASCADE)

    def __str__(self):
        return self.EpisodeName

    