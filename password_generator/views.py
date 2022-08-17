from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
	return render(request, "home.html", name = "test")

def about(request):
	return render(request, 'about.html', name = "test")

def password(request):
	password = ''
	length = int(request.GET.get('select'))
	letters = list('abcdefghijklmnopqrstuvwxyz')
	if request.GET.get('symbols') == 'on':
		letters.extend(list('!@#$%^&*()_+-='))
	if request.GET.get('numbers') == 'on':
		letters.extend(list('1234567890'))
	if request.GET.get('uppercase') == 'on':
		letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	for i in range(length):
		password += random.choice(letters)
	return render(request, "password.html", {'password' : password})