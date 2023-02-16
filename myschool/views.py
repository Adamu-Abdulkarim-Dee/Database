from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from myschool.models import Primary, PrimaryAlbum, Secondary, Contact, SecondaryAlbum, SchoolBoard, ResultClass, SectionPrimary
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView 
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PrimaryForms, SecondaryForm, EditSecondaryForm, ContactForm,PrimaryEditForms, EditBoardForm, ResultPrimaryForms, EditResultPrimaryForms
from django.db.models import Q
from django.conf import settings

# Create your views here.
def dashboard(request):

    return render(request, 'Dashboard.html')

def home(request):
    boards = SchoolBoard.objects.filter(user=request.user)
    return render(request, 'home.html', {'boards':boards})

def profile(request, slug):
    boards = get_object_or_404(SchoolBoard, slug=slug)

    board = SchoolBoard.objects.filter(user=request.user)

    return render(request, 'profile.html', {'boards':boards, 'board':board})



#Specifically for primary school.
def primary(request):
    albums = PrimaryAlbum.objects.filter(user=request.user)
    search_query = request.GET.get('search_query')
    if search_query:
        albums = PrimaryAlbum.objects.filter(
            Q(name__icontains=search_query)
        )
    return render(request, 'primary.html', {'albums': albums, 'search_query':search_query})

def primary_albums_views(request, pk):

    post = get_object_or_404(PrimaryAlbum, id=pk)

    my_album = PrimaryAlbum.objects.get(id=pk)

    primaries = Primary.objects.filter(year_of_graduation_id=my_album.pk)

    search_query = request.GET.get('search_query')
    if search_query:
        primaries = Primary.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    return render(request, 'view_album_primary.html', {'primaries': primaries, 
    'post':post, 'my_album':my_album, 
    'search_query':search_query})


def view_student_information_primary(request, pk):
    post = get_object_or_404(Primary, id=pk)

    prima = Primary.objects.get(id=pk)
    board = SchoolBoard.objects.get(user=request.user)
    return render(request, 'view_full_student_informations_primary.html', 
    {'post': post, 'prima': prima, 'board':board})


class Primary_album_form(CreateView):
    model = PrimaryAlbum
    fields = ['name']
    template_name = 'create_primary_albums.html'
    success_url = reverse_lazy('Primary')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Primary_album_form, self).form_valid(form)
    

class CreatePrimaryStudent(LoginRequiredMixin, CreateView):
    model = Primary
    form_class = PrimaryForms
    template_name = 'create_primary_student_information.html'
    success_url = reverse_lazy('Home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['year_of_graduation'].queryset = PrimaryAlbum.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePrimaryStudent, self).form_valid(form)

class XEditPrimary(UpdateView):
    model = Primary
    form_class = PrimaryEditForms
    template_name = 'edit_primary_student.html'
    success_url = reverse_lazy('Home')



class BDeletePrimary(DeleteView):
    model = Primary
    template_name = 'delete_primary_student.html'
    success_url = reverse_lazy('Home')










#Specifically for secondary school.
def secondary(request):
    albums = SecondaryAlbum.objects.filter(user=request.user)
    search_query = request.GET.get('search_query')
    if search_query:
        albums = PrimaryAlbum.objects.filter(
            Q(name__icontains=search_query)
        )
    return render(request, 'secondary/secondary.html',{'albums': albums, 'search_query':search_query})


def secondary_albums_views(request, pk):
    post = get_object_or_404(SecondaryAlbum, id=pk)

    my_album = SecondaryAlbum.objects.get(id=pk)

    secondaries = Secondary.objects.filter(year_of_graduation_id=my_album.pk)

    search_query = request.GET.get('search_query')
    if search_query:
        secondaries = Secondary.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    return render(request, 'secondary/view_album_secondary.html', {'secondaries':secondaries, 
    'post':post, 'my_album':my_album, 'search_query':search_query})


    
def view_Student_information_secondary(request, pk):
    post = get_object_or_404(Secondary, id=pk)
    
    second = Secondary.objects.get(id=pk)
    board = SchoolBoard.objects.get(user=request.user)
    return render(request, 'secondary/view_Student_secondary.html', 
    {'post':post, 'second': second, 'board':board})

class Secondary_album_form(CreateView):
    model = SecondaryAlbum
    fields = ['name']
    template_name = 'secondary/create_secondary_album.html'
    success_url = reverse_lazy('Secondary')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (Secondary_album_form, self).form_valid(form)


class CreateSecondaryStudent(LoginRequiredMixin, CreateView):
    model = Secondary
    form_class = SecondaryForm
    template_name = 'secondary/create_secondary_student_information.html'
    success_url = reverse_lazy('Home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['year_of_graduation'].queryset = SecondaryAlbum.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (CreateSecondaryStudent, self).form_valid(form)

class EditSecondary(UpdateView):
    model = Secondary
    form_class = EditSecondaryForm
    template_name = 'secondary/edit_secondary_student.html'
    success_url = reverse_lazy('Home')

class DeleteSecondary(DeleteView):
    model = Secondary
    template_name = 'secondary/delete_seconary_student.html'
    success_url = reverse_lazy('Home')



#This side is for the school Board

class Board(UpdateView):
    model = SchoolBoard
    form_class = EditBoardForm
    template_name = 'board.html'
    success_url = reverse_lazy('Home')




#User Registrations and Login/SignIn.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Invalid Credential') 
            return redirect('login')
    else:        
        return render(request, 'login.html')  




def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Or Username Already Taking')
                return redirect('Register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Taken')
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not Match')
            return redirect('Register') 

        return redirect ('/')     
    else:
        return render(request, 'signup.html')

def terms(request):
    return render(request, 'terms.html')

def about(request):
    return render(request, 'about.html')

class Contact(CreateView):
    model = Contact 
    form_class = ContactForm
    template_name='contact.html' 
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (Contact, self).form_valid(form) 




#This side is for payment.

def handle_payment(request):

    return render(request, 'payment.html')



def view_result_primary(request):
    reults = ResultClass.objects.filter(user=request.user)
    context = {
        'results':reults
    }
    return render(request, 'result/primary_result.html', context)

def result_view(request, pk):
    post = get_object_or_404(ResultClass, id=pk)

    result = ResultClass.objects.get(id=pk)

    all_results = SectionPrimary.objects.filter(class_of_id=result.pk)

    context = {
        'post':post,
        'result':result,
        'all_results':all_results
    }
    return render(request, 'result/result_view.html', context)

def View_Primary_result(request, pk):
    post = get_object_or_404(SectionPrimary, id=pk)
    result = SectionPrimary.objects.get(id=pk)
    board = SchoolBoard.objects.get(user=request.user)
    context = {
        'post':post,
        'result':result,
        'board':board
    }
    return render(request, 'result/full_result_primary.html', context)

class Result(CreateView):
    model = ResultClass
    fields = ['name']
    template_name = 'result/create_result_primary.html'
    success_url = reverse_lazy('Home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (Result, self).form_valid(form)

class CreateResult(CreateView):
    model = SectionPrimary
    form_class = ResultPrimaryForms
    template_name = 'result/create_result_primary_student.html'
    success_url = reverse_lazy('Home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['class_of'].queryset = ResultClass.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (CreateResult, self).form_valid(form)

class EditResult(UpdateView):
    model = SectionPrimary
    form_class = EditResultPrimaryForms
    template_name = 'result/edit_result_primary.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (EditResult, self).form_valid(form)

class DeletePrimaryResult(DeleteView):
    model = SectionPrimary
    template_name = 'result/delete_primary_result.html'
    success_url = reverse_lazy('Home')


