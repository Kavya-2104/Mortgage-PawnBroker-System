from django import forms

# from .models import Admin, Employee, Department, Product
from .models import Admin, Pawn, Custo


class DateInput(forms.DateInput):
    input_type = "date"

# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = "all"
#
# class UpdateDepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = "all"
#
class CustForm(forms.ModelForm):
    class Meta:
        model = Custo
        fields = "__all__"
        labels = {"Collateral":"Select Category"}

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class PawnForm(forms.ModelForm):
    class Meta:
        model = Pawn
        fields = "__all__"
        widgets = {"dob":DateInput(),
                   "password":forms.PasswordInput(),
                   'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}