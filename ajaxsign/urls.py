from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^$',views.signup,name='signup'),
    # url('new1',views.new1,name='new1'),
    url('Otp/',views.Otp,name='Otp'),
    # url('login/',views.login,name='login'),
    # url('authn',views.authn,name='authn'),
    url('validate_username/', views.validate_username, name='validate_username'),
    url('loginajax',views.loginajax,name='loginajax'),
    # url('signajax',views.signajax,name='signajax'),
    # url('ajax',views.ajax,name='ajax'),
    url('forget/',views.forget_pass,name='forget_pass'),
    url('forget_function/',views.new2,name='new2'),
    url(r'^validate/', views.validate, name='validate'),
    url('profile/',views.profile,name='profile'),
    url('otp_validate/',views.otp_validate,name='otp_validate'),
    url('Otp/p',views.p,name='p'),
]