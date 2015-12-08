from django.contrib.sites.models import Site


def g(request):
    domain = request.META['HTTP_X_FORWARDED_SERVER']
    site = Site.objects.get(domain=domain)
    ctx = {}
    ctx['site'] = site
    ctx['domain'] = domain
    return ctx
