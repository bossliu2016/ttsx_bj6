from django.conf.urls import url
import views
urlpatterns=[
    url('^add/$',views.add),
    url('^count/$',views.count),
    url('^$',views.index),
    url('^edit/$',views.edit),
    url('^del/$',views.delete),
    url('^order/$',views.order),
]
