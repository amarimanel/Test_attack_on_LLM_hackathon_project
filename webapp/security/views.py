from django.shortcuts import render

def home(request):
    return render(request, 'security/home.html')

def test_page(request):
    # C'est ici qu'on fera l'appel aux modèles plus tard
    return render(request, 'security/test.html')

def stats_page(request):
    return render(request, 'security/stats.html')