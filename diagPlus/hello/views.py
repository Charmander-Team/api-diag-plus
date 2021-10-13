from django.http import HttpResponse

# Display a message
def index(request):
    return HttpResponse("Hello, world !")