from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms.user_form import UserForm
from applicant.models import Applicant


def register(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            # Creating applicant model for that user
            Applicant.objects.create(user=user)
            applicant = Applicant.objects.get(user=user)
            applicant.full_name = user.get_full_name()
            applicant.email = user.email
            applicant.save()

            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    return render(request, 'user/register.html', {
        'form': UserForm(),
    })

# def profile(request):
#     profile = Profile.objects.filter(user=request.user).first()
#     if request.method == 'POST':
#         form = ProfileForm(instance=profile, data=request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile')
#     return render(request, 'user/profile.html', {
#                   'form': ProfileForm(instance=profile) 
#     })
