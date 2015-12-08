from django.db import models
from django.contrib.sites.models import Site


class SiteBahave(object):
    pass


class PaCT(SiteBahave):
    pass

PaCTBehave = PaCT()


class TWA(SiteBahave):
    pass

TWABehave = TWA()


def get_site_behave(self, domain):
    if 'twa' in domain:
        return TWABehave
    else:
        return PaCTBehave


class SiteProxy(Site):
    class Meta:
        proxy = True

    @property
    def behave(self):
        if 'twa' in self.domain:
            return TWABehave
        else:
            return PaCTBehave


class SiteMeta(models.Model):
    site = models.ForeignKey(Site)
    key = models.SlugField(max_length=30)
    value = models.TextField()
