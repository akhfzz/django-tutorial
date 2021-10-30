from django.http import HttpResponse

def viewer(request):
    return HttpResponse('views')