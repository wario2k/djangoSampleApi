from django.db import models

# Create your models here.
class President(models.Model):
    #holds first name and last name
    name = models.CharField(max_length=200)
    #date of birth
    birthday =  models.DateField()
    #place of birth
    birthplace = models.CharField(max_length=200)
    #date of death
    death_day = models.DateField()
    death_place = models.CharField(max_length=200)
#return all vals
def __str__(self):
        return self.name, self.birthday, self.birthplace, self.death_day, self.death_place