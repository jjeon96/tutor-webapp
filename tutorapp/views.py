from django.shortcuts import render

# Create your views here.
def stub(request):
    return render(request, 'tutorapp/stub.html', {})
