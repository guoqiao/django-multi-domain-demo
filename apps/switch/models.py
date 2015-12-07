from django.db import models
from django.contrib.sites.models import Site


class SiteProxy(Site):
    class Meta:
        proxy = True


class SiteMeta(models.Model):
    site = models.ForeignKey(Site)
    key = models.SlugField(max_length=30)
    value = models.TextField()
