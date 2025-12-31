from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class sign_up(View):
    template_name = 'Student_Authentication/sign_up.html'

    def get(self,request):
        form = UserCreationForm()
        print(form)
        context = {'form':form}
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Sign_In')
        return HttpResponse("Error While Registering User")
    

class sign_in(View):
    template_name = 'Student_Authentication/sign_in.html'

    def get(self,request):
        context = {}
        return render(request,self.template_name,context)
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('Show_Student')
        return HttpResponse("Error Occur While Login The User")
    

class sign_out(View):
    def get(self,request):
        logout(request)
        return redirect('Sign_Up')