from django.shortcuts import render

from .models import Item

def index(request):
    items = []
    for i in range(2):
        item = Item()
        item.name = "p" + str(i)
        item.description = item.name + " description"
        item.price = 50.0 * i
        items.append(item)
    return render(request, 'index.html', {'items': items})
