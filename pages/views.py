from django.shortcuts import render


def home(request):
    context={
        'title':'home', 
        'features': [
            'Django', 
            'Templates', 
            'Static Files'
            ]
    }
    return render(request, 'home.html', context)
def about(request):
    return render(request,  'about.html', {'title':'about'})

def hello(request, name):
    return render(request, 'hello.html', {'name': name})
