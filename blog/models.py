from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=50)
  content = models.CharField(max_length=300)
  def __unicode__(self):
    return self.title