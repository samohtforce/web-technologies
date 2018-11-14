from django.urls import path
from django.conf.urls import url
from pharmacies import views

app_name = 'pharamacies'
urlpatterns = [
    url(r'^(?P<pharmacy_id>\d+)/(?P<slug>[-\w]+)/$', views.pharmacy_detail, name='pharmacy_detail')
]