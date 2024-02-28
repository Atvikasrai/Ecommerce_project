from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings
from .forms import LoginForm, ResetPasswordForm, ChangePasswordForm, PasswordSetForm
#---------------------------


urlpatterns = [
    #user
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    
    #-----------------------------------------------------------------------------------
    path('address/', views.addressview, name = 'address'),   
    
    #-----------------------------------------------------------------------------------
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name = 'updateAddress'),  
    
    #-----------------------------------------------------------------------------------


    #Login Authentication
    path('registration',views.RegistrationFormView.as_view(), name = 'registration'),
    
    #-----------------------------------------------------------------------------------
    path('accounts/login/', auth_view.LoginView.as_view(template_name='user/login.html', authentication_form=LoginForm), name='login'),
    
    #-----------------------------------------------------------------------------------
    path('logout/', views.logoutview , name='logout'),

    #-----------------------------------------------------------------------------------
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='user/changepassword.html', form_class=ChangePasswordForm, success_url = '/passwordchangedone'), name='changepassword'),

    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='user/passwordchangedone.html'), name='passwordchangedone'),

    #-----------------------------------------------------------------------------------
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='user/resetpassword.html', form_class=ResetPasswordForm), name='resetpassword'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirmation/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html', form_class=PasswordSetForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),












] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)