from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, ProfileForm
from django.contrib import messages
from .models import Customer
from django.contrib.auth import *


# Create your views here.
#-----------------------------------------------------------------------------------------------------
class RegistrationFormView(View):
    def get(sel, request):
        form = RegistrationForm()
        return render(request, "user/registration.html", locals())
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulation! On your Successful Registration")
        else:
            messages.warning(request, "Invalid input data please check.!")
        return render(request, "user/registration.html", locals())
    
#-----------------------------------------------------------------------------------------------------
class ProfileView(View):
    def get(self,request):
        form = ProfileForm()
        return render(request, 'user/profile.html', locals())
    def post(self,request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name']
            last_name   = form.cleaned_data['last_name']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            pincode = form.cleaned_data['pincode']
            state = form.cleaned_data['state']
            

            reg = Customer(user=user, first_name=first_name, last_name=last_name, contact=contact, email=email, locality=locality, city=city, pincode=pincode, state=state)

            reg.save()
            messages.success(request, 'Congratulation! Prfile Save successfully')
        else:
            messages.warning(request, 'Invalid Data Please Check.!')
        return render(request, 'user/profile.html', locals())
    
#-----------------------------------------------------------------------------------------------------
def addressview(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'user/address.html', locals())

#-----------------------------------------------------------------------------------------------------
class updateAddress(View):
    def get(self, request, pk ):
        add =Customer.objects.get(pk=pk)
        form =ProfileForm(instance=add)
        return render(request,'user/updateAddress.html', locals())
    def post(self, request, pk):
        form =ProfileForm(request.POST)
        if form.is_valid():
            
            add =Customer.objects.get(pk=pk)
            add.first_name = form.cleaned_data['first_name']
            add.last_name   = form.cleaned_data['last_name']
            add.email = form.cleaned_data['email']
            add.locality = form.cleaned_data['locality']
            add.contact = form.cleaned_data['contact']
            add.city = form.cleaned_data['city']
            add.pincode = form.cleaned_data['pincode']
            add.state = form.cleaned_data['state']
           

            add.save()
            messages.success(request, 'Congratulation! Prfile Save successfully')
        
        else:
            messages.warning(request, 'Invalid Data Please Check.!')

        return redirect('address')
#-----------------------------------------------------------------------------------------------------
class ChangePasswordView(View):
    pass

#-----------------------------------------------------------------------------------------------------
class ResetPasswordView(View):
    pass


#-----------------------------------------------------------------------------------------------------
def logoutview(request):
    if request.method == 'POST':
        logout(request)
        messages.success(
            request,
            'You have been logged out'
        )
        return redirect('login')
    return render(request, 'user/logout.html')
