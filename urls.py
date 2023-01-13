from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.views.generic import RedirectView
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.cutie),
    #path('', views.home),
    path('cute', views.cute,name="cute"),
    path("next",views.next,name='next'),
    path("pro",views.house,name='pro'),
    #path("pro",views.hello,name='pro'),
    path("update_item/",views.decent,name='checkout'),
    #path("xoxo",views.trick,name='trick'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico')),
    #path(r'^my_def_in_view$',views.hh,name='my_def_in_view')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
