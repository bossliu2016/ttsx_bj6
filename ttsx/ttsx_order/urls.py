from django.conf.urls import url
import views
urlpatterns=[
    url('^$',views.do_order),
]
