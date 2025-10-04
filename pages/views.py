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

def gallery(request):#for images
    images = ['image.jpg', 'image2.jpg', 'image3.jpg']
    return render(request , 'gallery.html', {'images': images})

def page_not_found_view(request, exception):
    return render(request , '404.html', status=404)

def server_error_view(request):
    return render(request , '500.html', status=500)