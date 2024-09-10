from django.shortcuts import render

def show_main(request):
    context = {
        'name_aplikasi': 'albinstore',
        'name': 'Alvin',
        'npm' : '2306275866',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)