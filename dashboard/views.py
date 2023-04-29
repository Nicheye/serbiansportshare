from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.
from item.models import Item
@login_required
def index(request,user):
    user = request.user
    items = Item.objects.filter(created_by=user)
    return render(request,'dashboard/index.html',{
        'items':items,
    })