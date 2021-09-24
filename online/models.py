from django.db import models

# Create your models here.

class itemsmodel(models.Model):
    itemname = models.CharField(max_length=30)
    def __str__(self):
        return str(self.itemname)
    
class productmodel(models.Model):
    pname= models.CharField(max_length=30)
    pdesc= models.CharField(max_length=50)
    pprice= models.FloatField()
    pdiscount= models.FloatField()
    ppic = models.ImageField()
    itemid=models.ForeignKey(itemsmodel, on_delete=models.CASCADE)
    
    
    
