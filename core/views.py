from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Student
from .forms import AddStudentForm, SignUpForm, LoginForm


# ----------------- AUTH -----------------

def signupPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            print("SIGNUP ERRORS:", form.errors)
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
        else:
            print("LOGIN ERRORS:", form.errors)
    else:
        form = LoginForm()

    return render(request, "core/login.html", {"form": form})


def logoutPage(request):
    logout(request)
    return redirect("login")


# ----------------- HOME -----------------

class Home(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, "core/home.html", {"stu_data": stu_data})


# ----------------- CRUD -----------------

class AddStudent(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        form = AddStudentForm()
        return render(request, "core/add_student.html", {"form": form})

    def post(self, request):
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, "core/add_student.html", {"form": form})


class UpdateStudent(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = AddStudentForm(instance=student)
        return render(request, "core/update_student.html", {"form": form, "student": student})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, "core/update_student.html", {"form": form, "student": student})


class DeleteStudent(LoginRequiredMixin, View):
    login_url = "login"

    def post(self, request):
        student_id = request.POST.get("id")
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect("home")
