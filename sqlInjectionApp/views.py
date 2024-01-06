from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import userLogin
from .forms import loginForm
def is_admin_present(username):
    return "admin" in username.lower()
# Create your views here.
def login(request):
    form = loginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        if  is_admin_present(username) and password:  # Check if password is not empty
            # Simulate SQL injection by removing the password check using SQL comment sequence --
            user_query = 'SELECT * FROM sqlInjectionApp_userLogin WHERE username = "{}" AND password = "{}"'.format(username, password)
            user = userLogin.objects.raw(user_query)
            

            if user:
                
                return HttpResponse("Congratulations The flag is : LakshayCTF{$QLI_26}")
        
        return render(request, 'sqlInjectionApp/login.html', {'form': form, 'error_message': 'Login failed'})
    
    return render(request, 'sqlInjectionApp/login.html', {'form': form})


