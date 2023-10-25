from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from .forms import AdminLoginForm, PawnForm, CustForm
from .models import Admin, Pawn, Custo


def index(request):
    return render(request, "index.html")

def pawnregister(request):
    form = PawnForm()
    if request.method == "POST":
        formdata = PawnForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg = "User Registered Successfully"
            return render(request, "pawnlogin.html", {"pawnform": form, "msg": msg})
        else:
            msg = "Failed to Register User"
            return render(request, "pawnreg.html", {"pawnform": form, "msg": msg})
    return render(request, "pawnreg.html", {"pawnform": form})


def pawnlogin(request):
    return render(request, "pawnlogin.html")

def checkpawnlogin(request):
    uname = request.POST["eusername"]
    pwd = request.POST["epassword"]

    flag = Pawn.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        emp = Pawn.objects.get(username=uname)
        print(emp)
        request.session["eid"] = emp.id
        request.session["ename"] = emp.fullname
        return render(request, "userhome.html", {"eid": emp.id, "ename": emp.fullname})
    else:
        msg = "Login Failed"
        return render(request, "pawnlogin.html", {"msg": msg})

#
def userhome(request):
    eid = request.session["eid"]
    ename = request.session["ename"]

    return render(request, "userhome.html", {"eid": eid, "ename": ename})


def pawnprof(request):
    eid = request.session["eid"]
    ename = request.session["ename"]
    emp = Pawn.objects.get(id=eid)
    return render(request, "pawnprof.html", {"eid": eid, "ename": ename, "emp": emp})


def pawnpwdch(request):
    eid = request.session["eid"]
    ename = request.session["ename"]
    return render(request, "pawnpwdch.html", {"eid": eid, "ename": ename})

#
def pawnpwdup(request):
    eid = request.session["eid"]
    ename = request.session["ename"]

    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]

    flag = Pawn.objects.filter(Q(id=eid) & Q(password=opwd))

    if flag:
        Pawn.objects.filter(id=eid).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "pawnpwdch.html", {"eid": eid, "ename": ename, "msg": msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "pawnpwdch.html", {"eid": eid, "ename": ename, "msg": msg})


def emplogout(request):
    return render(request, "pawnlogin.html")


def adminlogin(request):
    return render(request, "adminlogin.html")
def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})
def adminhome(request):
    auname = request.session["auname"]
    return render(request, "adminhome.html", {"auname": auname})

def adminlogout(request):
    return render(request,"adminlogin.html")

def viewemployees(request):
    auname=request.session["auname"]
    emplist = Pawn.objects.all()
    count = Pawn.objects.count()
    return render(request,"viewusers.html",{"auname":auname,"emplist":emplist,"count":count})

def search(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Custo.objects.filter(Q(first_name__icontains=search_post))
    return render(request,"search.html",{'posts':posts})

def sortID(request):
    search_post = request.GET.get('sort')
    pos = Custo.objects.all()
    if search_post == 'sort':
        pos = pos.all().order_by('-amt')
    # Add more conditions here for other fields to sort on
    return render(request, "sort.html", {'posts': pos})





def viewadmincust(request):
    auname=request.session["auname"]
    productlist = Custo.objects.all()
    count = Custo.objects.count()
    return render(request,"viewadmincust.html",{"auname":auname,"productlist":productlist,"count":count})

def deleteemp(request,eid):
    Pawn.objects.filter(id=eid).delete()
    return redirect("viewusers.html")



def addproduct(request):
    auname = request.session["auname"]
    form = CustForm()
    if request.method == "POST":
        formdata = CustForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "listdisplay.html", {"auname":auname,"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addcustomer.html", {"auname":auname,"productform": form, "msg": msg})
    return render(request,"addcustomer.html",{"auname":auname,"productform":form})






















def viewusercust(request):
    pro = Custo.objects.all()
    return render(request, "listdisplay.html", {"pro": pro})

# def displayusercust(request):
#     eid = request.session["eid"]
#     ename = request.session["ename"]
#     cname = request.POST["cname"]
#     print(cname)
#     productlist = Custo.objects.filter(name__icontains=cname)
#     return render(request, "displayusercust.html", {"eid": eid, "ename": ename, "productlist": productlist})
# def displayusercust(request):
#     eid = request.session["eid"]
#     ename = request.session["ename"]
#     cname = request.POST["cname"]
#     print(cname)
#     productlist = Custo.objects.filter(name__icontains=cname)
#     return render(request, "displayusercust.html", {"eid": eid, "ename": ename, "productlist": productlist})
#


class SearchResultsView(ListView):
    model = Custo
    template_name = "search_prof.html"
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Custo.objects.filter(
            Q(first_name__icontains=query)
        )
        return object_list














































#
# def viewdepartments(request):
#     auname=request.session["auname"]
#     deptlist = Department.objects.all()
#     count = Department.objects.count()
#     return render(request,"viewdepts.html",{"auname":auname,"deptlist":deptlist,"count":count})
#
# def viewaproducts(request):
#     auname=request.session["auname"]
#     productlist = Product.objects.all()
#     count = Product.objects.count()
#     return render(request,"viewadmincust.html",{"auname":auname,"productlist":productlist,"count":count})
#
# def deleteemp(reequest,eid):
#     Employee.objects.filter(id=eid).delete()
#     return redirect("viewemps")
#
#
# def vieweproducts(request):
#     eid = request.session["eid"]
#     ename = request.session["ename"]
#
#     productlist = Product.objects.all()
#
#     return render(request, "viewusercust.html", {"eid": eid, "ename": ename, "productlist": productlist})
#
#
# def displayeproducts(request):
#     eid = request.session["eid"]
#     ename = request.session["ename"]
#
#     pname = request.POST["pname"]
#     print(pname)
#
#     productlist = Product.objects.filter(name__icontains=pname)
#
#     return render(request, "displayusercust.html", {"eid": eid, "ename": ename, "productlist": productlist})
#
#
# def adddepartment(request):
#     auname = request.session["auname"]
#     form = DepartmentForm()
#     if request.method == "POST":
#         formdata = DepartmentForm(request.POST)
#         if formdata.is_valid():
#             formdata.save()
#             msg="Department Added Successfully"
#             return render(request, "adddept.html", {"auname":auname,"deptform": form,"msg":msg})
#         else:
#             msg = "Failed to Add Department"
#             return render(request, "adddept.html", {"auname":auname,"deptform": form, "msg": msg})
#     return render(request,"adddept.html",{"auname":auname,"deptform":form})
#
# def updatedepartment(request):
#     auname = request.session["auname"]
#     form = UpdateDepartmentForm()
#     if request.method == "POST":
#         formdata = UpdateDepartmentForm(request.POST)
#
#         deptid = formdata.data['id']
#         deptname = formdata.data['name']
#         deptloc = formdata.data['location']
#
#         flag = Department.objects.filter(id=deptid)
#
#         if flag:
#             Department.objects.filter(id=deptid).update(name=deptname,location=deptloc)
#             msg="Department Updated Successfully"
#             return render(request, "updatedept.html", {"auname":auname,"deptform": form,"msg":msg})
#         else:
#             msg = "Department ID Not Found"
#             return render(request, "updatedept.html", {"auname":auname,"deptform": form, "msg": msg})
#
#     return render(request,"updatedept.html",{"auname":auname,"deptform":form})
#
# def addproduct(request):
#     auname = request.session["auname"]
#     form = ProductForm()
#     if request.method == "POST":
#         formdata = ProductForm(request.POST,request.FILES)
#         if formdata.is_valid():
#             formdata.save()
#             msg="Product Added Successfully"
#             return render(request, "addcustomer.html", {"auname":auname,"productform": form,"msg":msg})
#         else:
#             msg = "Failed to Add Product"
#             return render(request, "addcustomer.html", {"auname":auname,"productform": form, "msg": msg})
#     return render(request,"addcustomer.html",{"auname":auname,"productform":form})
#