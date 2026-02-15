from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from .forms import AddStudentForm


class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html', {'stu_data': stu_data})


class AddStudent(View):
    def get(self, request):
        form = AddStudentForm()
        return render(request, 'core/add_student.html', {'form': form})

    def post(self, request):
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'core/add_student.html', {'form': form})


class UpdateStudent(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = AddStudentForm(instance=student)
        return render(request, 'core/update_student.html', {'form': form, 'student': student})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'core/update_student.html', {'form': form, 'student': student})


class DeleteStudent(View):
    def post(self, request):
        student_id = request.POST.get('id')
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('home')
