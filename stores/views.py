from django.http import HttpResponse
from .models import Store


def index(request):
    store_list = Store.objects.all()
    output = ",".join([store.name for store in store_list])
    return HttpResponse(output)