from django.db import models

class event(models.Model):
    class Meta:
        db_table = 'events'

    event_id= models.AutoField(primary_key=True)
    event_name= models.CharField(max_length=50, blank=False, null=False)
    date= models.DateField(blank=False, null=False)
    location= models.CharField(max_length=50, blank=False, null=False)
    description= models.TextField(max_length=400, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.event_name
