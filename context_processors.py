from django.contrib.sites.models import Site

site = Site.objects.get_current()

def g(request):
    ctx = {}
    ctx['site'] = site
    domain = request.META['HTTP_X_FORWARDED_SERVER']
    ctx['domain'] = domain
    return ctx
