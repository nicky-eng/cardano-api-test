from django.http import HttpResponse
from django.template import loader

from .models import Store


def index(request):
    store_list = Store.objects.all()
    template = loader.get_template("stores/index.html")
    context = {
        "store_list": store_list,
    }
    return HttpResponse(template.render(context, request))