from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import templates
from .forms import LoginForm,SignUpForm,SellMenuForm,CustomerForm,SaleBillForm,VehicleAddForm,SaleDetailForm,RentMenuForm,RentDetailForm,UpdateForm
from django.contrib.auth import authenticate, login,logout
from django.views.generic import View
from .models import Admin,Dealer,Vehicle,Customer,Csales,Crent
from django.db import transaction
def home(request):
	if request.method == 'GET':
		return render(request,'home.html')

	if request.method == 'POST':
		return render(request,'home.html')	
		
def dbms(request):
	return render(request,'dbms.html')

def forgot(request):
	return render(request,'forgot.html')

def sale(request):
	return render(request,'sale.html')

def rent(request):
	return render(request,'rent.html')

def repair(request):
	return render(request,'repair.html')

def contact(request):
	if request.method=="POST":
		return redirect('/cdms/home')
	if request.method == "GET":	
		return render(request,'contact.html')

def custdetails(request):
	return render(request,'cust_details.html')

def saledetails(request):
	return render(request,'sale_details.html')

def salebill(request):
	form=SaleBill

	if request.method == 'GET':
		return form.get(form,request)

	if request.method == 'POST':
		return form.post(form,request)		


def signup(request):
	form=SignUpFormView

	if request.method == 'GET':
		return form.get(form,request)

	if request.method == 'POST':
		return form.post(form,request)

def custsignup(request):
	form=CustomerSignUp

	if request.method == 'GET':
		return form.get(form,request)

	if request.method == 'POST':
		return form.post(form,request)

def addcar(request):
	form=VehicleAdd

	if request.method == 'GET':
		return form.get(form,request)

	if request.method == 'POST':
		return form.post(form,request)


def saledetail(request):
	form=SaleDetail

	if request.method == 'GET':
		return form.get(form,request)

	if request.method == 'POST':
		return form.post(form,request)


def rentdetail(request):
	form=RentDetail

	if request.method == 'GET':
		return form.get(form,request)

	if request.method == 'POST':
		return form.post(form,request)		


def signin(request):
	if request.method=='GET':
		return render(request,'login.html',)
	
	if request.method=='POST':
		u=request.POST['username']
		p=request.POST['password']
		user=Admin.objects.all().filter(username=u).filter(password=p)
		#user=authenticate(username=username,password=password)
		#return render(request,'login.html',)
		if user:
			#login(request,user)
			return render(request,'index.html') 
			#return HttpResponse("hello")
	return render(request,'login.html')

class SignUpFormView():
	form_class = SignUpForm
	template_name = 'register.html'

	def get(self, request):
		form=self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#process form data

	def post(self, request):
		form= self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)

			#cleaned normalized data
			fname=form.cleaned_data['fname']
			lname=form.cleaned_data['lname']
			username=form.cleaned_data['username']
			#email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			#user.set_password(password)
			contactnumber=form.cleaned_data['contactnumber']
			address=form.cleaned_data['address']
			pincode=form.cleaned_data['pincode']
			
			user.save()
			return render(request,'index.html')

def update(request):
	form=UpdateFormView

	if request.method == 'GET':
		return form.get(form,request)
	if request.method == 'POST':
		return form.post(form,request)


class UpdateFormView():
	form_class=UpdateForm
	template_name= 'update.html'

	def get(self, request):
		form=self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)
			vehid=form.cleaned_data['vehid']	
			vehname=form.cleaned_data['vehname']
			vehmodel=form.cleaned_data['vehmodel']
			vehtype=form.cleaned_data['vehtype']
			vehcost=form.cleaned_data['vehcost']
			#createdat=form.cleaned_data['createdat']
			status=form.cleaned_data['status']
			repcost=form.cleaned_data['repcost']	
			rentcost_perday=form.cleaned_data['rentcost_perday']
			a=Vehicle.objects.all().filter(vehid=vehid)
			for object in a:
				object.vehname=vehname
				object.vehmodel=vehmodel
				object.vehtype=vehtype
				object.vehcost=vehcost
				object.status=status
				object.repcost=repcost
				object.rentcost_perday=rentcost_perday
				object.save()	
			#user.save()

			return render(request,'index.html')	
		return render(request,'update.html')

class CustomerSignUp():
	form_class = CustomerForm
	template_name = 'cust_details.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name, {'form':form})

	def post(self,request):
		form= self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)
			custid=form.cleaned_data['custid']	
			fname=form.cleaned_data['fname']
			lname=form.cleaned_data['lname']
			contactno=form.cleaned_data['contactno']
			emailid=form.cleaned_data['emailid']
			password=form.cleaned_data['password']
			address=form.cleaned_data['address']
			gender=form.cleaned_data['gender']
			lastlogin=form.cleaned_data['lastlogin']	

			user.save()
			return redirect('/cdms/saledetail')
	
		return render(request,'cust_details.html')	


class VehicleAdd():
	form_class = VehicleAddForm
	template_name = 'add_car.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name, {'form':form})

	def post(self,request):
		form= self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)		
			
			vehname=form.cleaned_data['vehname']
			vehmodel=form.cleaned_data['vehmodel']
			vehtype=form.cleaned_data['vehtype']
			vehcost=form.cleaned_data['vehcost']
			createdat=form.cleaned_data['createdat']
			status=form.cleaned_data['status']
			repcost=form.cleaned_data['repcost']	
			rentcost_perday=form.cleaned_data['rentcost_perday']
			colour=form.cleaned_data['colour']

			user.save()
			return render(request,'index.html')
	
		return render(request,'add_car.html')	

class SaleDetail():
	form_class = SaleDetailForm
	template_name = 'sale_details.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name, {'form':form})

	def post(self,request):
		form= self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)		
			vehid=form.cleaned_data['vehid']
			a=Vehicle.objects.all().filter(vehid=vehid)
			for object in a:
				object.status=1
				object.save()
			custid=form.cleaned_data['custid']
			dealerid=form.cleaned_data['dealerid']
			price=form.cleaned_data['price']
			saledate=form.cleaned_data['saledate']
			paidby=form.cleaned_data['paidby']
			#repcost=form.cleaned_data['repcost']	
			#rentcost_perday=form.cleaned_data['rentcost_perday']
			#colour=form.cleaned_data['colour']

			user.save()
			return render(request,'index.html')
	
		return render(request,'sale_details.html')	

class RentDetail():
	form_class = RentDetailForm
	template_name = 'rent_details.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name, {'form':form})

	def post(self,request):
		form= self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)		
			custid=form.cleaned_data['custid']
			dealerid=form.cleaned_data['dealerid']
			vehid=form.cleaned_data['vehid']
			a=Vehicle.objects.all().filter(vehid=vehid)
			for object in a:
				object.status=2
				object.save()
			price=form.cleaned_data['price']
			rentdate=form.cleaned_data['rentdate']
			returndate=	form.cleaned_data['returndate']
			#colour=form.cleaned_data['colour']			

			user.save()
			return render(request,'index.html')
	
		return render(request,'rent_details.html')	




class SaleBill():
	form_class= SaleBillForm
	template_name= 'sale.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name, {'form':form})

	def post(self,request):
		form= self.form_class(request.POST)
		
		if form.is_valid():
			#user=form.save(commit=False)
			a=form.cleaned_data['vehid']
			cars=Vehicle.objects.all().filter(vehid=a)
			return render(request,'sellmenu.html',{'form':form,'cars':cars})
		
		form=SaleBillForm()	
		return render(request,'sale.html',{'form':form})


def dealersignin(request):
	if request.method=='GET':
		return render(request,'admin_login.html',)
	
	if request.method=='POST':
		u=request.POST['username']
		p=request.POST['password']
		user=Dealer.objects.all().filter(username=u).filter(password=p)
		#user=authenticate(username=username,password=password)
		#return render(request,'login.html',)
		if user :
			#login(request,user)
			return render(request,'index.html') 
			#return HttpRespons
			e("hello")
	return render(request,'admin_login.html')


def sellmenu(request):
	if request.method=='POST':
		form=SellMenuForm(request.POST)
		if form.is_valid():
			b = form.cleaned_data['vehname']
			d = form.cleaned_data['vehtype']
			e = form.cleaned_data['vehmodel']
			f = form.cleaned_data['status']
 			#f = form.cleaned_data['status']
			if f and e and d and b:
				cars=Vehicle.objects.all().filter(status=f).filter(vehmodel=e).filter(vehtype=d).filter(vehname=b)
				return render(request,'sellmenu.html',{'form':form,'cars':cars})

			elif b and f :
				cars=Vehicle.objects.all().filter(vehname=b).filter(status=f)
				return render(request,'sellmenu.html',{'form':form,'cars':cars})
			elif d and f:
				cars=Vehicle.objects.all().filter(vehtype=d).filter(status=f)
				return render(request,'sellmenu.html',{'form':form,'cars':cars})
			elif e and f :
				cars=Vehicle.objects.all().filter(vehmodel=e).filter(status=f)
				return render(request,'sellmenu.html',{'form':form,'cars':cars})	
			
			elif b and d and f:
				cars=Vehicle.objects.all().filter(vehname=b).filter(vehtype=d).filter(status=f)
				return render(request,'sellmenu.html',{'form':form,'cars':cars})

			elif f:
				cars=Vehicle.objects.all().filter(status=f)
				return render(request,'sellmenu.html',{'form':form,'cars':cars})

			else :
				cars=Vehicle.objects.all().filter(vehname=b).filter(vehtype=d).filter(vehmodel=e)
				return render(request,'sellmenu.html',{'form':form,'cars':cars})

	form=SellMenuForm()
	return render(request,'sellmenu.html',{'form':form})

def rentmenu(request):
	if request.method=='POST':
		form=RentMenuForm(request.POST)
		if form.is_valid():
			b = form.cleaned_data['vehname']
			d = form.cleaned_data['vehtype']
			e = form.cleaned_data['vehmodel']
			f = form.cleaned_data['status']
 			#f = form.cleaned_data['status']
			if f and e and d and b:
				cars=Vehicle.objects.all().filter(status=f).filter(vehmodel=e).filter(vehtype=d).filter(vehname=b)
				return render(request,'rentmenu.html',{'form':form,'cars':cars})

			elif b and f :
				cars=Vehicle.objects.all().filter(vehname=b).filter(status=f)
				return render(request,'rentmenu.html',{'form':form,'cars':cars})
			elif d and f:
				cars=Vehicle.objects.all().filter(vehtype=d).filter(status=f)
				return render(request,'rentmenu.html',{'form':form,'cars':cars})
			elif e and f :
				cars=Vehicle.objects.all().filter(vehmodel=e).filter(status=f)
				return render(request,'rentmenu.html',{'form':form,'cars':cars})	
			
			elif b and d and f:
				cars=Vehicle.objects.all().filter(vehname=b).filter(vehtype=d).filter(status=f)
				return render(request,'rentmenu.html',{'form':form,'cars':cars})

			elif f:
				cars=Vehicle.objects.all().filter(status=f)
				return render(request,'rentmenu.html',{'form':form,'cars':cars})

			else :
				cars=Vehicle.objects.all().filter(vehname=b).filter(vehtype=d).filter(vehmodel=e)
				return render(request,'rentmenu.html',{'form':form,'cars':cars})

	form=RentMenuForm()
	return render(request,'rentmenu.html',{'form':form})


# Create your views here.
