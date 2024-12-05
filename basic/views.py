from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.

def home(request):        
    return render(request, 'home.html', {})
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have been successfully logged in')
            return redirect('data')
        else:
            messages.success(request, 'There was an error in logged in ...!')
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})
        

def logout_user(request):
    logout(request)
    messages.success(request, 'successfully logout...')
    return redirect('home')




def show_data(request):
    if request.user.is_authenticated:
        records=Record.objects.all()
        return render(request, 'data.html', {'records':records})
    
    else:
         messages.success(request, "You Must Be Logged In...")
         return redirect('login')



 
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'you have been successfully registered')
            return redirect('data')
        else:
            messages.success(request, 'There was an error in registration ...!')
            return redirect('register')
    else:
        form=SignUpForm()
    return render(request, 'register.html',{'form':form}) 


def user_record(request, pk):
    if request.user.is_authenticated:
        see_record=Record.objects.get(id=pk)
        return render(request, 'record.html',{'record':see_record})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('login')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully ...!')
        return redirect('data')
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('login')
    
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('data')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('login')
    

def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('data')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('login')

        
        