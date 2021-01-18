from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from contacts.models import Contact

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Username/Password is incorrect')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out successfully...')
        return redirect('index')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        #Checking Password
        if password == password2:

            # Check User Name
            if User.objects.filter(username=username).exists():
                messages.error(request, "UserName already exists")
                return redirect('register')
            else:

                #Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    #Everything looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    #auth.login(request,user)
                    #messages.success('You have logged in successfully...')
                    #return redirect('index')
                    messages.success(request, 'You are successfully registered, please login...')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts' : user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)