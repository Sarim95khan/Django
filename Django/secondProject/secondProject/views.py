from django.http import HttpResponse


def Header(request):
    return HttpResponse("<h1>Sarim AHmed khan</h1>")