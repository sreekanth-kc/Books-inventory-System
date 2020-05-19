# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from book_management.models import AppUser, Book
from django.contrib import admin

# Register your models here.
admin.site.register(AppUser, )
admin.site.register(Book)