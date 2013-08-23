from django.http import HttpResponse
from log.models import Log


def logo(request):
    ip = request.META.get('REMOTE_ADDR')
    print ip
    referer = request.META.get('HTTP_REFERER')
    print referer
    host = request.META.get('HTTP_HOST')
    print host
    useragent = request.META.get('HTTP_USER_AGENT')
    print useragent
    log = Log.objects.create(Ip=ip,Referer=referer,UserAgent=useragent)
    log.save()
    OPENID_LOGO_BASE_64 = """iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QgXCjEWoNS2gwAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAABG0lEQVQ4y+2VPU4DMRCFP0dwAiRouAVcwUYcBnGFtNTUtChncA4QRcou0FNCkaCcAJFH4bBstN5hN2ipGMnF/Oj5aWb87CSJgWzEgDYo+EHXwhBCIxZj/B34F2iM98AzaJESj1e1XMslMsx7L+lN0kz6OEpnxfcp0eaObV3TsIFn0uZWgIAd4CpmXGC3RQvQGK0yqVrMAUw6tqViXWtDjnnlz/PsRybrHuZO+u75ep1tQ87v94g0BuD88swEsPLtA31awykURYE7tuCLxGXZY8+991JZG15uj0nDVLnPKgK8gF7BOdckNgcOQQ8tQ7YkN4RAvJkm5z1TsAW+mPisBLif9LzSj+vpLutlArW0xXX9LPZRRff/E/05+Cc8Unt4j72pYwAAAABJRU5ErkJggg=="""
    return HttpResponse(
        OPENID_LOGO_BASE_64.decode('base64'), mimetype='image/png'
    )
# Logo from http://openid.net/login-bg.gif
# Embedded here for convenience; you should serve this as a static file
