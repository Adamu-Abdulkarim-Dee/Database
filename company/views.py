from django.shortcuts import render, redirect
from .forms import EditBoardForm, ContactForm, RegistrationForms, LoginForm
from .models import SchoolBoard, Contact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView 
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy



def login(request):

    return render(request, 'login.html')

def register(request):
    
    return render(request, 'register.html')



class Board(UpdateView):
    model = SchoolBoard
    form_class = EditBoardForm
    template_name = 'board.html'
    success_url = reverse_lazy('Home')


def about(request):
    return render(request, 'about.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def terms(request):
    return render(request, 'terms.html')

class Contact(CreateView):
    model = Contact 
    form_class = ContactForm
    template_name='contact.html' 
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (Contact, self).form_valid(form) 