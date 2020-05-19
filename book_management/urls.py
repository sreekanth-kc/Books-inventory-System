
from django.conf.urls import url
from book_management.views import (
Registration_view,
Login_View,
BorrowBook
)

urlpatterns = [
    url(r'^register/', Registration_view.as_view(), name='register'),
    url(r'^login/', Login_View.as_view(), name='login'),
    url(r'^bb/', BorrowBook.as_view(), name='bb')
]
