from django.http import HttpResponse

def about(request):
    return HttpResponse("ABOUT PAGE WORKING")