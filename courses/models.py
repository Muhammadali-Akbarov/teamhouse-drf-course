from enum import unique
from django.db import models



class Cource(models.Model):
    
    title = models.CharField(max_length=255)
    url   = models.URLField(unique=True)

    def __str__(self):
        
        return self.title
    
class Review(models.Model):
    
    cource      = models.ForeignKey(Cource,related_name="reviews",on_delete=models.CASCADE)
    name        = models.CharField(max_length=255)
    email       = models.EmailField()
    comment     = models.TextField(blank=True,default="")
    rating      = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True) 

    class Meta:
        unique_together =  ['email','cource']
    
    def __str__(self):
        return "{0.rating} by {0.email} for {0.cource}".format(self)


