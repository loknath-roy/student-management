
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewStudent
from .models import Student

# Create your views here.
def Home(request):
    return render(request,'myapp/home.html')
# REGISTRATION SECTION

def SignupPage(request):
    if request.method=='POST':
    
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
       
        if pass1 != pass2:
            messages.warning(request, " Your password and confirm password does not match" )
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request, "Congratulations! Account created successfully" )
        return redirect('login')
    return render(request,'myapp/signup.html')


# LOGIN SECTION

def LoginPage(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')

            user_obj=authenticate(username = username,password=password)
            if user_obj:
               login(request,user_obj)
               return redirect('add')
            messages.warning(request,"Wrong username or password")
            
            return redirect('login')
        
        except Exception as e:
            messages.error(request,"Something went wrong")
            return redirect('signup')

    return render(request,'myapp/login.html')


# THIS FUNCTION WILL ADD NEW STUDENT

@login_required(login_url='login')
def AddStudent(request):
    if request.method == 'POST':
        form = NewStudent(request.POST)
        nm = request.POST['name']
        cs = request.POST['course']
        rn = request.POST['rollno']
        dob = request.POST['dob']
        gn = request.POST['gender']
        em = request.POST['email']
        mb = request.POST['mobile']
        gmb = request.POST['guardian_mobile']
        new_std=Student(name=nm,course=cs,rollno=rn,dob=dob,gender=gn,email=em,mobile=mb,guardian_mobile=gmb)
        new_std.save()
        #form = NewStudent()
        #new_std=NewStudent()
        #return HttpResponseRedirect('')
        messages.success(request,"Student added successfully")
        return redirect('add')
        
    else:
        form = NewStudent()

    return render(request,'myapp/addStudent.html',{'form':form})

    
# THIS FUNCTION WILL VIEW ALL STUDENTS

@login_required(login_url='login')
def ViewStudent(request):
    stud = Student.objects.all()
    return render(request,'myapp/showStudent.html',{'student':stud})

# THIS FUNCTION WILL DELETE A PARTICULAR STUDENT

def DeleteStudent(request,id):
    if request.method=='POST':
        dl = Student.objects.get(pk=id)
        dl.delete()
        return redirect('view')

# LOGOUT SECTION

def LogOut(request):
    logout(request)
    return redirect('login')

# SEARCH SECTION

@login_required(login_url='login')
def Search(request):
        query = request.GET['query']
        if query == '':
            messages.warning(request,"Please enter any search keyword.")
            return render(request,'myapp/search.html')
            
        else:
            # User can search students by their name,course and roll no.
            student_name = Student.objects.filter(name__icontains=query)
            student_course = Student.objects.filter(course__icontains=query)
            student_roll = Student.objects.filter(rollno__icontains=query)
            student = student_name.union(student_roll,student_course)

            search = {'student': student,'query': query}
            return render(request,'myapp/search.html',search)
        
    
            





