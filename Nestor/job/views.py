from django.shortcuts import render

# Create your views here.

jobs = [
    { 'title': 'Software Engineer', 'company': 'Marel', 'percentage': '100', 'days': '12'},
    { 'title': 'Bank Engineer', 'company': 'Arion', 'percentage': '90', 'days': '123'},
    { 'title': 'Cunt Engineer', 'company': 'Islandsbanki', 'percentage': '25', 'days': '1'}
]

def index(request):
    return render(request, 'job/index.html', context={'jobs': jobs})