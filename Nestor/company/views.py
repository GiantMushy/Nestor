from django.shortcuts import render


# Create your views here.


companies = [
    { 'name': 'Islandsbanki', 'address': 'Heiðarás 5', 'phone': '661-5966', 'mail': 'islandsbanki@islandsbanki.is', 'available_jobs': 23},
    { 'name': 'Marel', 'address': 'Heiðarás 5', 'phone': '661-1234', 'mail': 'marel@islandsbanki.is', 'available_jobs': 243},
    { 'name': 'Össur', 'address': 'Gusti 5', 'phone': '432-1234', 'mail': 'ossur@islandsbanki.is', 'available_jobs': 2},
]

def index(request):
    return render(request, 'company/index.html', context={'companies': companies})