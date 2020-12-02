from django.http import HttpResponse
from django.utils.translation import ugettext as _

def index(request):
    message = _("Hello, world. You're at the translation index.")
    return HttpResponse(message)