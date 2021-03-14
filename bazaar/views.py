from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import UserRegistrationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User, Cart , Product , Customer

# Create your views here.
#from django.views.generic import TemplateView


#home page
class IndexView(View):
    def get(self, request): 
       mobile = Product.objects.filter(category='M')         
       laptop = Product.objects.filter(category='L')         
       topwear = Product.objects.filter(category='TW')         
       bottomwear = Product.objects.filter(category='BW')         
       return render(request , 'bazaar/index.html',{'mobile':mobile , 'laptop':laptop , 'topwear':topwear,'bottomwear':bottomwear})

# signup       
class UserRegistration(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request ,'bazaar/userregistration.html' , {'form':form})  
        

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():         
            messages.success(request, 'Congratulations!! Registered Successfully.')          
            form.save()           
        return render(request, 'bazaar/userregistration.html',{'form':form})
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # pass1 = form.cleaned_data['password1']
            # pass2 = form.cleaned_data['password2']         
            # data = User(username = username,email = email, password = pass1 )
            # data.save()
         
#productDetailView
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'bazaar/productdetailview.html',{'product':product})      
        

            
    