from django.http import HttpResponse, HttpResponseNotFound
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)




def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')


def my_view2(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)        


def my_view404(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')     