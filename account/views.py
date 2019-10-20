from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def indexView(request):
    return render(request,'index.html')
def registerView(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form =UserCreationForm()
    return render(request,'registration/register.html',{'form':form})
