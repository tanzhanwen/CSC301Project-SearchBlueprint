from django.db import models

# Create your models here.
class Note(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title + " " + self.body
