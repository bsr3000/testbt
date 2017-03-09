from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Position(models.Model):
    pos_name = models.CharField(max_length=75, verbose_name="Position name")

    def __str__(self):
        return u"%s" % self.pos_name

    def __unicode__(self):
        return u"%s" % self.pos_name


class Group(models.Model):
    gr_name = models.CharField(max_length=75, verbose_name="Group name")

    def __str__(self):
        return u"%s" % self.gr_name

    def __unicode__(self):
        return u"%s" % self.gr_name


class User(AbstractUser):
    group = models.ForeignKey(Group, blank=True, null=True, verbose_name="Group")
    position = models.ForeignKey(Position, blank=True, null=True, verbose_name="Position")
    salary = models.PositiveIntegerField(blank=True, null=False, verbose_name="Salary", default=0)
    photo = models.ImageField(upload_to="user_photos/", blank=True, null=False, default='user_photos/default.jpg')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return u"%s" % self.email

    def __unicode__(self):
        return u"%s" % self.email


def upload_file_name(docs, filename):
    return u'user_docs/%s/%s' % (str(docs.user.email), filename)


class UserDocs(models.Model):
    user = models.ForeignKey(User)
    doc = models.FileField(upload_to=upload_file_name)

    def __str__(self):
        return u"%s" % self.user_id

    def __unicode__(self):
        return u"%s" % self.user_id