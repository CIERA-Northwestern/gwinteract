from django.db import models

# Create your models here.

class GWEvent(models.Model):
    superevent_id = models.CharField(max_length=10)
    gw_id = models.CharField(max_length=10, default=None, null=True, blank=True)
    preferred_event = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)    
    posteriors_uploaded = models.BooleanField(default=False)
    skymap_uploaded = models.BooleanField(default=False)
    redshift_uploaded = models.BooleanField(default=False)
