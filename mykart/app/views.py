from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,OrderPlaced,Cart,Product
from .forms import CustomerRegistrationForm,LoginForm
from django.http import HttpResponse
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')
class Productview(View):
 def get(self,request):
  topwears=Product.objects.filter(category='TW')
  bag=Product.objects.filter(category='Bag')
  mobiles=Product.objects.filter(category='M')
  laptops=Product.objects.filter(category='L')
  return render(request, 'app/home.html',{'topwears':topwears,'bag':bag,'mobiles':mobiles,'laptops':laptops})
# --------------------------------------------------------------------------------------------------------------
# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class Productdetailview(View):
 def get(self,request,pk):
  product=Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html',{'product':product})
# ------------------------------------------------------------------------------
def mobile(request,mob=None):
  if mob==None:
   mobiles=Product.objects.filter(category='M')
  elif mob =='redmi' or mob=='iphone':
   mobiles = Product.objects.filter(category='M').filter(brand=mob)
  elif mob<='22000':
   mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=22000)
  elif mob>='30000':
   mobiles = Product.objects.filter(category='M').filter(discounted_price__gte=30000)
  else:
   mobiles = Product.objects.filter(category='M').exclude(discounted_price__exact=48000)
  return render(request, 'app/mobile.html',{'mobiles':mobiles})
# -----------------------------------------------------------------------------------------------------

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
 def get(self,r):
  form=CustomerRegistrationForm()
  return render(r,'app/customerregistration.html',{'form':form})
 def post(self,r):
  form=CustomerRegistrationForm(r.POST)
  if form.is_valid():
   messages.success(r,'congrats for registration')
   form.save()
   return HttpResponse('thank you')
  return render(r,'app/customerregistration.html',{'form':form})
# ---------------------------------------------------------------------------

# def login(request):
#  form=LoginForm()
#  return render(request, 'app/login.html',{'form':form})

# -----------------------------------------------------------------

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')


def checkout(request):
 return render(request, 'app/checkout.html')
