from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('pawnbroker_registration',views.pawnregister,name="pawnreg"),
    path('pawnbroker_login',views.pawnlogin,name="pawnlogin"),
    path('checkpawnbroker_login',views.checkpawnlogin,name="checkpawnlogin"),
    path('userhome',views.userhome,name="userhome"),
    path('pawnprofile',views.pawnprof,name="pawnprof"),
    path('pawnpwdchange',views.pawnpwdch,name="pawnpwdch"),
    path('pawnpwdup', views.pawnpwdup, name="pawnpwdup"),
    path('emplogout',views.emplogout,name='emplogout'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('viewemps',views.viewemployees,name="viewemps"),
     path('adminlogout', views.adminlogout, name='adminlogout'),
    path("deleteemp/<int:eid>", views.deleteemp, name="deleteemp"),
    path("addproduct", views.addproduct, name="addproduct"),
    path("viewadmincust", views.viewadmincust, name="viewadmincust"),
    path("viewusercust", views.viewusercust, name="viewusercust"),

    path('search', views.search, name="search"),
    path('sort', views.sortID, name="sort"),
    #      path("displayusercust", views.displayusercust, name="displayusercust"),
# #

    # path("search/", views.SearchResultsView.as_view(), name="search_prof"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

























#     path('viewdepts',views.viewdepartments,name="viewdepts"),

#     path("adddept",views.adddepartment,name="adddept"),
#     path("updatedept",views.updatedepartment,name="updatedept"),
