from django.conf.urls import url
from . import templates,views
app_name = 'cdms'

urlpatterns =[
	url(r'^signin/', views.signin, name='signin'),
	url(r'^dbms/',views.dbms, name='dbms'),
	url(r'^update/',views.update, name='update'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^saledetail/', views.saledetail, name='saledetail'),
	url(r'^saledetails/', views.saledetails, name='saledetails'),
	url(r'^rentdetail/', views.rentdetail, name='rentdetail'),
	url(r'^addcar/', views.addcar, name='addcar'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^home/', views.home, name='home'),
	url(r'^forgot/', views.forgot, name='forgot'),
	url(r'^dealersignin/', views.dealersignin, name='dealersignin'),
	url(r'^sale/', views.sale, name='sale'),
	url(r'^rent/', views.rent, name='rent'),
	url(r'^repair/', views.repair, name='repair'),
	url(r'^sellmenu/', views.sellmenu, name='sellmenu'),
	url(r'^rentmenu/', views.rentmenu, name='rentmenu'),
	url(r'^custsignup/', views.custsignup, name='custsignup'),
	url(r'^custdetails/', views.custdetails, name='custdetails'),
	url(r'^salebill/', views.salebill, name='salebill')
	
]
