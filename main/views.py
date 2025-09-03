from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406358900',
        'name': 'Friliani Gloria',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

# Create your views here.
