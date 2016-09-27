from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

def index(request):
	return redirect('/main')

def main(request):
	return render(request, 'logreg/index.html')

def login(request):
	result = User.objects.validateLog(request)

	if result[0] == False:
		print_messages(request, result[1])
		return redirect('/')
	else:
		return loguserin(request, result[1])

def register(request, id):
	result = User.objects.validateReg(request)

	if result[0] == False:
		print_messages(request, result[1])
		return redirect('/')
	else:
		request.session["user_id"] = user.id
		return redirect('/success')

def success(request):
	if not 'user' in request.session:
		return redirect('/')
	else:
		return redirect('/dashboard')

def print_messages(request, message_list):
	for message in message_list:
		messages.add_message(request, messages.INFO, message)

def loguserin(request, user):
    request.session['user'] = {
        'id' : user.name,
        'name' : user.name,
        'username' : user.username,
    }
    return redirect('/success')

def logout(request):
	request.session.pop('user')
	return redirect('/')