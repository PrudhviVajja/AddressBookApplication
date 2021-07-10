from django.urls import path
from .views import * 
# ContactList, ContactDetail, ContactCreate, RegisterView, ContactUpdate, ContactDelete, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', ContactList.as_view(), name='contacts'),
    path('contact/<int:pk>/', ContactDetail.as_view(), name='contact'),
    path('contact-create/', ContactCreate.as_view(), name='contact-create'),
    path('contact-update/<int:pk>/', ContactUpdate.as_view(), name='contact-update'),
    path('contact-delete/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),
    
]