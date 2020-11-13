from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from asset.models import Transfer, Acquisition
from django.contrib.auth.models import User



@login_required(login_url='login')
def home(request):
	written = Transfer.objects.filter(is_active=False).count()
	recent = Acquisition.objects.all().order_by('date_acquired')[:7]
	active_asset = Transfer.objects.filter(is_active=True).count()
	alluser = User.objects.all().count()
	

	context = {
		'written':written,
		'title':'Home',
		'active_asset':active_asset,
		'alluser': alluser,
		'recent':recent,
		
	}

	return render(request, 'asset/dashboard.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password =request.POST['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			
			else:
				messages.info(request, 'Username or password is incorrect.')
		
		context = {}
		return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')


