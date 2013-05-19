from django.db import models

class LikeRouter(object):
    """
    Route all requests for models in this app to a seperate db
    """
    def read_db(self, model, **hints):
        if model._meta.app_label == 'likethis' :
            return 'wantit'
        return None
    def write_db(self, model, **hints):
        if model._meta.app_label == 'likethis' :
            return 'wantit'
        return None

        
# Create your models here.
class Want(models.Model):
    item = models.CharField(max_length=120)
    last_wanted = models.DateTimeField('last searched')        

    def __unicode__(self):
        return self.item

class FoundItem(models.Model):
    item_wanted = models.ForeignKey(Want)
    item_url = models.CharField(max_length=200)
    wants = models.IntegerField(default=0)

    def __unicode__(self):
        return self.item_url
