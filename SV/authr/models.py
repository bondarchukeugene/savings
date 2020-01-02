from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo (models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    group_title = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.username


class UserGroup (models.Model):

    group_title = models.ForeignKey('UserProfileInfo',on_delete=models.SET_NULL,null=True)
    total_funds = models.CharField(max_length=200)

    def __str__(self):
        return self.group_title

class UserPMT (models.Model):

    user = models.ForeignKey('UserProfileInfo', on_delete=models.SET_NULL, null=True)
    pmt_dt = models.DateField(auto_now=False,auto_now_add=True)
    pmt_amt = models.CharField(max_length=200)