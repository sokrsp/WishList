from django.shortcuts import render, redirect
from .models import Item
from ..logreg.models import User
# Create your views here.
def index(request):
	context = {
		'items' : Item.objects.all(),
		'users' : User.objects.all()
	}
	return render(request, 'dashboard/index.html', context)


def destroy(request, id):
	itemDelete = Item.objects.get(id=id)
	itemDelete.delete()
	return redirect('/dashboard')