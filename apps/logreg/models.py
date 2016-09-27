from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re

class UserManager(models.Manager):
	def validateLog(self, request):
		
		try:
			user = User.objects.get(username = request.POST['username'])

			password = request.POST['password'].encode()
			if bcrypt.hashpw(password, user.pw.encode()) == user.pw.encode():
				return (True, user)

		except ObjectDoesNotExist:
			pass
		return (False, ['Incorrect Username/Password'])
	def validateReg(self, request):
		errors = self.validateInputs(request)
		if len(errors) > 0:
			return(False, errors)
		pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

		user = self.create(name=request.POST['name'], username=request.POST['username'], pw=pw, birthday=request.POST['birthday'])
		return (True, user)

	def validateInputs(self, request):
		errors = []
		if len(request.POST['name']) <= 2:
			errors.append('Name must be at least 3 characters long')
		if len(request.POST['username']) <= 2:
			errors.append('Username must be at least 3 characters long')
		if len(request.POST['password']) < 8:
			errors.append('Password must be atleast 8 characters')
		if request.POST['password'] != request.POST['confirmpassword']:
			errors.append('Passwords do not match')
		if not request.POST['birthday']:
			errors.append('Please enter date of birth')
		return errors
		
class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=55)
	pw = models.CharField(max_length=100)
	birthday = models.DateField()

	objects = UserManager()