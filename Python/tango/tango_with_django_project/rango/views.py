from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	#return HttpResponse("Rango says hey there world!")
	context_dict = {'boldmessage':"I am bold font form the context"}
	return render(request,'rango/index.html',context_dict)
