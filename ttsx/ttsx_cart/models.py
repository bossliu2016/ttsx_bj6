#coding=utf-8
from django.db import models
from ttsx_goods.models import GoodsInfo
# Create your models here.
class CartInfo(models.Model):
    #谁买了多少个什么
    user=models.ForeignKey('ttsx_user.UserInfo')
    goods=models.ForeignKey(GoodsInfo)
    count=models.IntegerField()
