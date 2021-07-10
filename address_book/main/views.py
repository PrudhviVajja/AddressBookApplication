from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import Contact

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('contacts')
    
class RegisterView(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('contacts')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('contacts')
        return super(RegisterView, self).get(*args, **kwargs)

class ContactList(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = context['contacts'].filter(user=self.request.user)
        context['count'] = context['contacts'].filter(first_name=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['contacts'] = context['contacts'].filter(first_name__icontains=search_input)
        context['search_input'] = search_input
        return context
    
class ContactDetail(LoginRequiredMixin, DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'main/detail.html'
    
class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'address', 'email', 'phone']
    template_name = 'main/create.html'
    success_url = reverse_lazy('contacts')
    # context_object_name = 'createcontact'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ContactCreate, self).form_valid(form)
    
    
class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'address', 'email', 'phone']
    template_name = 'main/create.html'
    # template_name = 'main/update.html'
    success_url = reverse_lazy('contacts')
    
class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'main/delete.html'
    success_url = reverse_lazy('contacts')
