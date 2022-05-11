from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .utils import id_generator
import datetime
from datetime import timedelta
from django.utils.timezone import make_aware
# Create your models here.





class WikiSearch(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    views = models.BigIntegerField(default=0)
    unique_id = models.CharField(max_length=20,db_index=True)
    is_published = models.BooleanField(default=True)
    external_link = models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Wiki Search' 
        verbose_name_plural = 'Wiki Searches'   
    

    def save(self, *args, **kwargs):    
        if not self.unique_id:
            self.unique_id = id_generator()
            while WikiSearch.objects.filter(unique_id=self.unique_id).exists():
                self.unique_id = id_generator()
        super(WikiSearch, self).save()

    def __str__(self):
        return self.title +" - " + self.unique_id

