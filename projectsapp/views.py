from django.shortcuts import redirect, render
from . models import Project,Contactus,Feedback
from django.contrib import messages
# Create your views here.

def index(request):
	return render(request,"index.html")

def projects(request):
	projects = Project.objects.all()
	dic = {'projects':projects}
	return render(request,'projects.html',dic)	


def contact(request):
	
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		number = request.POST.get("number")
		msg = request.POST.get("msg")
		contact = Contactus(name = name , email = email , number = number , msg = msg)
		contact.save()
		messages.success(request,"Message Has Been Sent! Thanks For Contact Us")
		return redirect("contact")
	return render(request,"contactus.html")	

def feedback(request):
	
	if request.method == "POST":
		name = request.POST.get("name")
		msg = request.POST.get("msg")
		feedback = Feedback(name = name , msg = msg)
		feedback.save()
		messages.success(request,"Message Has Been Sent! Thanks For Sharing your feed Back")
		return redirect("feedback")
	return render(request,"feedback.html")	


def about(request):
	return render(request,"about.html")

