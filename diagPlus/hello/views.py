from django.http import HttpResponse
from django.shortcuts import render

from .models import User

# Display a message
def index(request):
    list_all_user = User.objects.all()
    context = {
        'list_all_user': list_all_user,
    }
    return render(request, 'hello/index.html', context)

def detail(request, user_id):

    return HttpResponse('User %s' % user_id)