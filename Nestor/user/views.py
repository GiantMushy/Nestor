from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms.user_form import UserForm
from applicant.forms.applicant_form import ApplicantForm

def register(request):

    # for message in messages:
    #     # Do something with each message, e.g., print or process
    #     print(message)
    if request.method =='POST':
        form = UserForm(data=request.POST)
        form2 = ApplicantForm(data=request.POST)
        if form.is_valid():
            form.save()
            print("form 1 valid")
            print(form.id)
            print(request.user)
            form2.user = request.user
            if form2.is_valid():
                form2.save()
            
                return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    return render(request, 'user/register.html', {
        'form': UserForm(),
        'form2': ApplicantForm()
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
