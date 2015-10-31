from django.db import models

# Create your models here.
class BaseExercise(models.Model):
    muscle_group = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    youtube_link = models.CharField(max_length=128, blank=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.muscle_group ,self.name)
    
    class Meta:
        unique_together = ('name', 'muscle_group',)
