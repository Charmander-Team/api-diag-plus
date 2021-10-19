from django.http import HttpResponse
from django.template import loader

from .models import User

# Display a message
def index(request):
    list_all_user = User.objects.all()
    template = loader.get_template('hello/index.html')
    context = {
        'list_all_user': list_all_user,
    }
    return HttpResponse(template.render(context, request))

def detail(request, user_id):

    return HttpResponse('User %s' % user_id)