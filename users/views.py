from django.shortcuts import render, redirect
from .forms import SignupForm, UpdateProfileForm
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import CustomUser, Saved
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from products.models import Product
# Create your views here.


class SignupView(UserPassesTestMixin,View):
    def get(self, request):
        return render(request, 'registration/signup.html', {'form':SignupForm()})
    
    def post(self, request):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully created.')
            return redirect('login')
        return render(request, 'registration/signup.html', {'form':form} )    
    
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return False
        return True
            
class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'profile.html', {'customuser':user})         
    
class UpdateProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = UpdateProfileForm(instance=request.user)   
        return render(request, 'profile_update.html', {'form':form}) 
    
    def post(self, request):
        form = UpdateProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully updated.')
            return redirect('users:profile', request.user)
        return render(request, 'registration/signup.html', {'form':form} )    
    
    
class AddRemoveSavedView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        saved_product = Saved.objects.filter(author=request.user, product=product)
        if saved_product:
            saved_product.delete()
            messages.info(request, 'Removed.')  
        else:
            Saved.objects.create(author=request.user, product=product)    
            messages.info(request, 'Saved.')  
        return redirect(request.META.get("HTTP_REFERER"))    


class SavedView(LoginRequiredMixin, View):
    login_url='login'
    def get(self, request):
        saveds = Saved.objects.filter(author=request.user)  
        q=request.GET.get('q', '')
        if q:
            products = Product.objects.filter(title__icontains=q) 
            saveds = Saved.objects.filter(author=request.user, product__in=products)
        return render(request, 'saveds.html', {"saveds":saveds}) 
    
class RecentlyViewedView(View):
    def get(self, request):
        if not "recently_viewed" in request.session:
            products =[]
        else:
            r_viewed = request.session["recently_viewed"]
            products = Product.objects.filter(id__in = r_viewed)
            q=request.GET.get('q', '')
            if q:
                products = products.filter(title__icontains=q)
        return render(request, "recently_viewed.html", {'products':products})    
                        