from django.shortcuts import render, redirect
from ..dashboard.models import Item

def create(request):
	return render(request, 'wish_items/create.html')

def process(request):
	Item.objects.create(itemname=request.POST['itemname'])
	return redirect('/dashboard')

def viewproduct(request, id):

	return render(request, 'dashboard/viewproduct.html')
