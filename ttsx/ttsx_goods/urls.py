from django.conf.urls import url
import views
urlpatterns=[
    url('^$',views.index),
    url(r'^list(\d+)_(\d+)/$',views.goods_list),
    url(r'^(\d+)/$',views.detail),
]
