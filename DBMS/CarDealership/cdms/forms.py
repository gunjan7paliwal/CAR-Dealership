from .models import Admin
from .models import Customer
from .models import Dealer
from .models import Vehicle
from .models import Sales,Csales
from .models import Rent,Crent
from django import forms

class SaleBillForm(forms.ModelForm):
	vehid = forms.CharField(max_length=25)

	class Meta:
		model = Vehicle
		fields=['vehid']


class LoginForm(forms.ModelForm):
	username = forms.CharField(max_length = 100)
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta:
		model = Admin
		fields=['username','password']

class SignUpForm(forms.ModelForm):
	fname = forms.CharField(max_length=25)
	lname = forms.CharField(max_length=25)
	username = forms.CharField(max_length=25)
	password = forms.CharField(widget = forms.PasswordInput())
	contactnumber = forms.CharField(max_length=25)
	address = forms.CharField()
	#lastlogin = models.DateTimeField(blank=True, null=True)
	pincode = forms.CharField(max_length=20)

	#lastlogin = forms.DateTimeField(blank=True, null=True)

	class Meta:
		model = Dealer
		fields=['fname','lname','username','password','contactnumber','address','pincode']

class UpdateForm(forms.ModelForm):
	vehid= forms.CharField(max_length=25)
	vehname = forms.CharField(max_length=25,required=False)
	vehmodel = forms.CharField(max_length=25,required=False)
	vehtype = forms.CharField(max_length=25,required=False)
	#taxid = forms.CharField(max_length=25)
	vehcost = forms.CharField(max_length=25,required=False)
	#createdat = forms.CharField(max_length=25,required=False)
	status = forms.CharField(max_length=25,required=False)
	repcost = forms.CharField(max_length=25,required=False)
	rentcost_perday = forms.CharField(max_length=25,required=False)
	
	class Meta:
		model = Vehicle
		fields=['vehid','vehname','vehmodel','vehtype','vehcost','status','repcost','rentcost_perday']		

class SellMenuForm(forms.Form):
	vehname = forms.CharField(max_length=25,required=False)
	vehtype = forms.CharField(max_length=25,required=False)
	vehmodel = forms.CharField(max_length=25,required=False)
	status = forms.CharField(max_length=25,required=False)

class RentMenuForm(forms.Form):
	vehname = forms.CharField(max_length=25,required=False)
	vehtype = forms.CharField(max_length=25,required=False)
	vehmodel = forms.CharField(max_length=25,required=False)
	status = forms.CharField(max_length=25,required=False)


class CustomerForm(forms.ModelForm):
	custid = forms.CharField(max_length=25)
	fname = forms.CharField(max_length=25)
	lname = forms.CharField(max_length=25)
	contactno = forms.CharField(max_length=25)
	emailid = forms.CharField(max_length=25)
	password = forms.CharField(widget = forms.PasswordInput())
	address = forms.CharField(max_length=25)
	#pincode = forms.CharField(max_length=25)
	gender = forms.CharField(max_length=25)	
	#lastlogin = forms.DateTimeField(blank=True,null=True)

	class Meta:
		model = Customer
		fields=['custid','fname','lname','contactno','emailid','password','address','gender','lastlogin']


class VehicleAddForm(forms.ModelForm):
	vehname = forms.CharField(max_length=25)
	vehmodel = forms.CharField(max_length=25)
	vehtype = forms.CharField(max_length=25)
	#taxid = forms.CharField(max_length=25)
	vehcost = forms.CharField(max_length=25)
	createdat = forms.CharField(max_length=25)
	status = forms.CharField(max_length=25)
	repcost = forms.CharField(max_length=25)
	rentcost_perday = forms.CharField(max_length=25)
	colour= forms.CharField(max_length=25)

	class Meta:
		model = Vehicle
		fields=['vehname','vehmodel','vehtype','vehcost','createdat','status','repcost','rentcost_perday','colour']

class SaleDetailForm(forms.ModelForm):

	vehid= forms.CharField(max_length=25)
	custid= forms.CharField(max_length=25)
	dealerid= forms.CharField(max_length=25)
	price= forms.CharField(max_length=25)
	saledate= forms.CharField(max_length=25)
	paidby= forms.CharField(max_length=25)

	class Meta:
		model = Csales
		fields=['vehid','custid','dealerid','price','saledate','paidby']

class RentDetailForm(forms.ModelForm):
	
	custid=forms.CharField(max_length=25)
	dealerid=forms.CharField(max_length=25)
	vehid=forms.CharField(max_length=25)
	price=forms.CharField(max_length=25)
	rentdate=forms.CharField(max_length=25)
	returndate=forms.CharField(max_length=25)

	class Meta:
		model = Crent
		fields=['custid','dealerid','vehid','price','rentdate','returndate']