# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Admin(models.Model):
    adminid = models.IntegerField(primary_key=True)
    adminfname = models.CharField(max_length=20, blank=True, null=True)
    adminlname = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=25, blank=True, null=True)
    contactnumber = models.CharField(max_length=25, blank=True, null=True)
    lastlogin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Crent(models.Model):
    rentid = models.AutoField(primary_key=True)
    custid = models.IntegerField(blank=True, null=True)
    dealerid = models.IntegerField(blank=True, null=True)
    vehid = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    rentdate = models.DateField(blank=True, null=True)
    returndate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crent'


class Csales(models.Model):
    vehid = models.IntegerField(blank=True, null=True)
    custid = models.IntegerField(blank=True, null=True)
    dealerid = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    saledate = models.DateField(blank=True, null=True)
    paidby = models.CharField(max_length=20, blank=True, null=True)
    saleid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'csales'



class CustPincode(models.Model):
    pincode = models.AutoField(primary_key=True, max_length=10)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_pincode'


class Customer(models.Model):
    custid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=25, blank=True, null=True)
    lname = models.CharField(max_length=25, blank=True, null=True)
    contactno = models.CharField(max_length=25, blank=True, null=True)
    emailid = models.CharField(max_length=35, blank=True, null=True)
    password = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    lastlogin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Dealer(models.Model):
    dealerid = models.AutoField(primary_key=True)
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminid', blank=True, null=True)
    fname = models.CharField(max_length=25, blank=True, null=True)
    lname = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=25, blank=True, null=True)
    contactnumber = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    lastlogin = models.DateTimeField(blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'dealer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Rent(models.Model):
    rentid = models.IntegerField(primary_key=True)
    vehid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehid', blank=True, null=True)
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='custid', blank=True, null=True)
    dealerid = models.ForeignKey(Dealer, models.DO_NOTHING, db_column='dealerid', blank=True, null=True)
    rentcost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    taxid = models.ForeignKey('Tax', models.DO_NOTHING, db_column='taxid', blank=True, null=True)
    rentdate = models.DateField(blank=True, null=True)
    returndate = models.DateField(blank=True, null=True)
    paidby = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rent'


class Repair(models.Model):
    repairid = models.IntegerField(primary_key=True)
    vehid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehid', blank=True, null=True)
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='custid', blank=True, null=True)
    dealerid = models.ForeignKey(Dealer, models.DO_NOTHING, db_column='dealerid', blank=True, null=True)
    repcost = models.FloatField(blank=True, null=True)
    taxid = models.ForeignKey('Tax', models.DO_NOTHING, db_column='taxid', blank=True, null=True)
    repairdate = models.DateField(blank=True, null=True)
    paidby = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair'


class Sales(models.Model):
    salesid = models.AutoField(primary_key=True)
    vehid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehid', blank=True, null=True)
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='custid', blank=True, null=True)
    dealerid = models.ForeignKey(Dealer, models.DO_NOTHING, db_column='dealerid', blank=True, null=True)
    salecost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    taxid = models.ForeignKey('Tax', models.DO_NOTHING, db_column='taxid', blank=True, null=True)
    saledate = models.DateField(blank=True, null=True)
    paidby = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class Tax(models.Model):
    taxid = models.AutoField(primary_key=True)
    taxdescription = models.TextField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax'


class Vehicle(models.Model):
    vehid = models.AutoField(primary_key=True)
    vehname = models.CharField(max_length=50, blank=True, null=True)
    vehmodel = models.CharField(max_length=50, blank=True, null=True)
    vehtype = models.CharField(max_length=15, blank=True, null=True)
    #taxid = models.ForeignKey(Tax, models.DO_NOTHING, db_column='taxid', blank=True, null=True)
    vehcost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createdat = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    repcost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rentcost_perday = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    colour = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle'
