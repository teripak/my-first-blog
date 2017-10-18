from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requerst):
	return HttpResponse("hello world! You are at the polls index.")

