from django.shortcuts import redirect, render
from . models import Project,Contactus,Feedback,Skill
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.

def index(request):
	return render(request,"index.html")

def projects(request):
	projects = Project.objects.all().order_by('-num')
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
	skills = Skill.objects.all().order_by('-num')
	return render(request,"about.html" , {'skills':skills})


def ulogin(request):
	user = request.user
	if request.method == "POST":
		name = request.POST.get("name")
		password = request.POST.get("password")
		user=authenticate(username= name, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Successfully Logged In")
				
			if not user.is_authenticated:
				messages.error(request, "You Are Not Logged In")
			if user.is_authenticated:
				return redirect("index")
			else:
				messages.error(request, "Invalid credentials! Please try again")
				# return redirect("home")
	
	return render(request,"login.html",{'user':user})



	
def ulogout(request):
	user=request.user
	if user.is_authenticated:
		logout(request)
		messages.success(request, "Successfully Logout..!")
	return redirect("index")


