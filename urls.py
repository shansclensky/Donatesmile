from django.conf.urls import include , url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from donatelove.views import landing_page

app_name = 'donatelove'

urlpatterns = [
    url(r'^$', landing_page),
    url(r'^donatelove/', include('donatelove.urls')),
    url(r'^admin/', admin.site.urls),
]
