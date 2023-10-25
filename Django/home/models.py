from django.db import models

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def str(self):
        return self.username

    class Meta:
        db_table = "admin_table"
class Pawn(models.Model):
    id=models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dob=models.CharField(max_length=20,blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)
    PawnlicenseID = models.CharField(max_length=10, blank=False)
    image = models.FileField(blank=True, upload_to="proffiles")

    def str(self):
      return self.fullname

    class Meta:
      db_table = "pawnbroker_table"

class Custo(models.Model):
    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=16,blank=False)
    contact = models.PositiveIntegerField(blank=False)
    interest = models.FloatField(max_length=4,blank=False)
    amt = models.PositiveIntegerField(blank=False)
    months = models.PositiveIntegerField(blank=False)
    category_choices = (
    ("Gold", "Gold"), ("Vehicles", "Vehicles"), ("Land Docs", "Land Docs"), ("Other Valuables", "Other Valuables"))
    Collateral = models.CharField(max_length=100, blank=False, choices=category_choices)
    Verified_ch = [(False, 'No'), (True, 'Yes')]
    Verified = models.BooleanField("Verified?", default=False,
                                       choices=Verified_ch,blank=False)
    Address =  models.CharField(max_length=40)
    image = models.FileField(blank=False,upload_to="Custimg")

    def str(self):
        return self.name

    class Meta:
        db_table = "cust_table"










































# class Department(models.Model):
#     id=models.PositiveIntegerField(primary_key=True, verbose_name="Department Id")
#     name = models.CharField(max_length=100, blank=False, unique=True, verbose_name="Department Name")
#     location = models.CharField(max_length=100, blank=False, verbose_name="Department Location")
#
#     def str(self):
#         return self.name
#
#     class Meta:
#         db_table = "department_table"
#
# class Employee(models.Model):
#     id=models.AutoField(primary_key=True)
#     fullname=models.CharField(max_length=100,blank=False)
#     gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
#     gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
#     dateofbirth=models.CharField(max_length=20,blank=False)
#     department = models.ForeignKey(Department,on_delete=models.CASCADE)
#     salary=models.PositiveIntegerField(blank=False)
#     email=models.EmailField(max_length=50,blank=False,unique=True)
#     username=models.CharField(max_length=50,blank=False,unique=True)
#     password = models.CharField(max_length=50, blank=False)
#     location = models.CharField(max_length=50, blank=False)
#     contact = models.BigIntegerField(blank=False,unique=True)
#     registrationtime = models.DateTimeField(blank=False,auto_now=True)
#
#     def str(self):
#         return self.fullname
#
#     class Meta:
#         db_table = "employee_table"
#
# class Product(models.Model):
#     id=models.AutoField(primary_key=True)
#     category_choices = (("Home", "Home"), ("Jewelry", "Jewelry"), ("Electronics", "Electronics"), ("Clothes","Clothers"),("Others","Others"))
#     category = models.CharField(max_length=100, blank=False,choices=category_choices)
#     name = models.CharField(max_length=100, blank=False)
#     description = models.TextField(max_length=200,blank=False)
#     price = models.PositiveIntegerField(blank=False)
#     image = models.FileField(blank=False,upload_to="productimages")
#
#     def str(self):
#         return self.name
#
#     class Meta:
#         db_table = "product_table"