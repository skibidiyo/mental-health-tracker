from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306256236',
        'name': 'Anindiyo Banu',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)