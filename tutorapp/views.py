from django.shortcuts import render

# Create your views here.
def stub(request):
    return render(request, 'tutorapp/stub.html', {})

def login(request):
	return render(request, 'tutorapp/login.html', {})

# def logout(request):
# 	return render(request, 'tutorapp/stub.html', {})
