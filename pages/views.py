from django.shortcuts import render 

announcements = [
    {'id': 1, 'title': 'New Library Opening', 'content': 'We are excited to announce our new library opening this week! The library will feature modern facilities, digital access, and much more.'},
    {'id': 2, 'title': 'Maintenance Notice', 'content': 'Our website will be down for maintenance from 12 AM to 3 AM this Saturday.'},
]

def home(request):
    context = {
        'title': 'home',
        'features': ['Home', 'Announcement', 'Nav Bar']
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'about'})

def hello(request, name):
    return render(request, 'hello.html', {'name': name})

def gallery(request):
    images = ['image.jpg', 'image2.jpg', 'image3.jpg']
    return render(request, 'gallery.html', {'images': images})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

def announcement_list(request):
    return render(request, 'announcement_list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = next((a for a in announcements if a['id'] == id), None)
    return render(request, 'announcement_detail.html', {'announcement': announcement})
