from django.db import models

# Create your models here.

class beer (models.Model):
    price = models.IntegerField()
    taste = models.CharField(max_length = 400)
    turnover = models.FloatField()
    description = models.CharField(max_length = 1000)
    main = models.CharField(max_length = 200, blank = True)
    img = models.ImageField(upload_to="myapp/static/img" , blank=True)
    
    def __str__(self):
        return self.main 
    
    
    
    
    
    
    
class Animals(models.Model):
    
    name = models.CharField(max_length = 100)    
    action = models.CharField(max_length = 100)    

    def does(self):
          return f'The "{self.name}" does "{self.action}"' 