from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name ="index" ),
    path("<str:name>",views.greet, name="greet"),
    path("mbali",views.mbali, name="Mbali"),
    path("kagisho",views.kagisho, name="kagisho"),
    

]