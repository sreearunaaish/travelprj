from . import views
from django.urls import path

urlpatterns = [
    # path('',views.detail,name='detail')
    # path('', views.contact, name='contact'),
    path('', views.index, name='index'),
   # path('arithmetic/', views.arith_metic, name='arith_metic')
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]

'''
urlpatterns = [

    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    ]
      '''

