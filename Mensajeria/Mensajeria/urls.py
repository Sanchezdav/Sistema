from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from app.views import *

urlpatterns = patterns('',
  
    url(r'^$', 'app.views.listing', name='servicios'),
    url(r'^table/$', 'app.views.listingTable', name='table'),
    url(r'^finalizar/$', 'app.views.listing2', name='finalizar'),
    url(r'^servicios/$', ServiciosForm.as_view(), name='serviciosform'),
    url(r'^ingresar/$', 'django.contrib.auth.views.login', {'template_name':'ingresar.html'},name='login'),
    url(r'^salir/$', 'django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^enterado/(?P<id_servicio>\d+)$','app.views.enterado'), 
    url(r'^finalizar/(?P<id_servicio>\d+)$','app.views.finalizar'), 

    url(r'^report_builder/', include('report_builder.urls')),
  
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
