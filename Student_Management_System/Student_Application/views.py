from django.shortcuts import render,redirect,get_object_or_404  
from django.views import View
from .forms import StudentForm
from django.http import HttpResponse
from .models import Student
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class create_student(LoginRequiredMixin,View):
    login_url = reverse_lazy('Sign_In')
    template_name = 'Student_Application/create_student.html'
    form = StudentForm()

    def get(self,request):
        context = {'form':self.form}
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = StudentForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
        return HttpResponse("Error Occurs While Saving Data")
    
class show_student(LoginRequiredMixin,View):
    login_url = reverse_lazy('Sign_In')
    template_name = 'Student_Application/show_student.html'

    def get(self,request):
        objs = Student.objects.all()
        context = {'records':objs}
        return render(request,self.template_name,context)    
    
class update_student(View):
    template_name = 'Student_Application/update_student.html'

    def get_object(self,pk):
        return get_object_or_404(Student,student_id=pk)

    def get(self,request,pk):
        obj = self.get_object(pk)
        form = StudentForm(instance=obj)
        context = {'form':form}
        return render(request,self.template_name,context)
    
    def post(self,request,pk):
        obj = self.get_object(pk)
        form = StudentForm(request.POST,request.FILES,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
        return HttpResponse("Error While Updating Records")
    
class delete_student(View):
    template_name = 'Student_Application/delete_student.html'

    def get_object(self,pk):
        return get_object_or_404(Student,student_id=pk)

    def get(self,request,pk):
        obj = self.get_object(pk)
        context = {'obj':obj}
        return render(request,self.template_name,context)
    
    def post(self,request,pk):
        obj = self.get_object(pk)
        obj.delete()
        return redirect('Show_Student')

