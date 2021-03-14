from django.urls import path
from bazaar import views 
from django.contrib.auth import views as auth_view
from.forms import UserLoginForm , UserChangePass , UserPasswordResetForm , UserSetPasswordForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('userregistration/',views.UserRegistration.as_view(), name='userregistration' ),
    path('accounts/login/', auth_view.LoginView.as_view(template_name = 'bazaar/userlogin.html' , authentication_form = UserLoginForm), name='userlogin'),
    path('logout/',auth_view.LogoutView.as_view(next_page='userlogin'),name='logout'),
    
    path('changepass/',auth_view.PasswordChangeView.as_view(form_class = UserChangePass,template_name = 'bazaar/userchangepass.html' , success_url='/passwordchangedone/'), name='userchangepass'),
    path('passwordchangedone/', auth_view.PasswordResetDoneView.as_view(template_name = 'bazaar/passwordchangedone.html'), name='passwordchangedone'),
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='bazaar/password_reset.html',form_class = UserPasswordResetForm),name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='bazaar/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='bazaar/password_reset_confirm.html' , form_class=UserSetPasswordForm ),name='password_reset_confirm'),
    path("password-reset-complete/", auth_view.PasswordResetCompleteView.as_view(template_name='bazaar/password_reset_complete.html'), name="password_reset_complete"),

    path('productdetail/<int:pk>/',views.ProductDetailView.as_view(), name='productdetail'),
    #path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

     