from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Primary, PrimaryResult, ScienceAlbums, Science, ArtAlbums, Art, AlbumC, AlbumA, AlbumS, CommerceAlbums, Commerce
from company.models import SchoolBoard
from .forms import EditPrimaryForms, PrimaryForms, EditScineceForms, ScineceForms, ArtForms, EditArtForms, CommerceForms, EditCommerceForms

# Create your views here.
def view_result_primary(request):
    reults = PrimaryResult.objects.filter(user=request.user)
    context = {
        'results':reults
    }
    return render(request, 'result/primary_result.html', context)

def result_view(request, pk):
    post = get_object_or_404(PrimaryResult, id=pk)

    result = PrimaryResult.objects.get(id=pk)

    all_results = Primary.objects.filter(class_of_id=result.pk)

    context = {
        'post':post,
        'result':result,
        'all_results':all_results
    }
    return render(request, 'result/result_view.html', context)

def View_Primary_result(request, pk):
    post = get_object_or_404(Primary, id=pk)
    result = Primary.objects.get(id=pk)
    board = SchoolBoard.objects.get(user=request.user)
    context = {
        'post':post,
        'result':result,
        'board':board
    }
    return render(request, 'result/full_result_primary.html', context)

class Result(CreateView):
    model = PrimaryResult
    fields = ['name']
    template_name = 'result/create_result_primary.html'
    success_url = reverse_lazy('Home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (Result, self).form_valid(form)

class CreateResult(CreateView):
    model = Primary
    form_class = PrimaryForms
    template_name = 'result/create_result_primary_student.html'
    success_url = reverse_lazy('Home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['class_of'].queryset = PrimaryResult.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (CreateResult, self).form_valid(form)

class EditResult(UpdateView):
    model = Primary
    form_class = EditPrimaryForms
    template_name = 'result/edit_result_primary.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (EditResult, self).form_valid(form)







def commerce(request):
    all_albums = AlbumC.objects.filter(user=request.user)
    context = {
        'all_albums':all_albums
    }
    return render(request, 'commerce/commerce.html', context)

def commerce_home(request):
    albums = CommerceAlbums.objects.filter(user=request.user)
    context = {
        'albums':albums
    }
    return render(request, 'commerce/commerce_home.html', context)

def commerce_view_albums(request, pk):
    post = get_object_or_404(CommerceAlbums, id=pk)

    result = CommerceAlbums.objects.get(id=pk)

    all_results = Commerce.objects.filter(class_of_id=result.pk)

    context = {
        'post':post,
        'result':result,
        'all_results':all_results
    }
    return render(request, 'commerce/commerce_view_albums.html', context)

def commerce_result_full(request, pk):
    post = get_object_or_404(Commerce, id=pk)
    result = Commerce.objects.get(id=pk)
    board = SchoolBoard.objects.get(user=request.user)
    context = {
        'post':post,
        'result':result,
        'board':board
    }
    return render(request, 'commerce/full_commerce_result.html', context)

class CreateCommerceResult(CreateView):
    model = CommerceAlbums
    form_class = CommerceForms
    template_name = 'commerce/create_result.html'
    success_url = reverse_lazy('Commerce')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['class_of'].queryset = CommerceAlbums.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (CreateCommerceResult, self).form_valid(form)

class CreateCommerceAlbums(CreateView):
    model = CommerceAlbums
    fields = ['name', 'albums']
    template_name = 'commerce/create_albums.html'
    success_url = reverse_lazy('Commerce')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['albums'].queryset = AlbumC.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (CreateCommerceAlbums, self).form_valid(form)

class EditCommerceResults(UpdateView):
    model = Commerce
    form_class = EditCommerceForms
    template_name = 'commerce/edit_result.html'
    success_url = reverse_lazy('Commerce')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (EditCommerceResults, self).form_valid(form)











def art_home(request):
    albums = ArtAlbums.objects.filter(user=request.user)
    context = {
        'albums':albums
    }
    return render(request, 'art/art_home.html', context)

def art_albums_view(request, pk):
    post = get_object_or_404(ArtAlbums, id=pk)

    result = ArtAlbums.objects.get(id=pk)

    all_results = Art.objects.filter(class_of_id=result.pk)

    context = {
        'post':post,
        'result':result,
        'all_results':all_results
    }
    return render(request, 'art/view_art_albums.html', context)

def art_result_full(request, pk):
    post = get_object_or_404(Art, id=pk)
    result = Art.objects.get(id=pk)
    board = SchoolBoard.objects.get(user=request.user)
    context = {
        'post':post,
        'result':result,
        'board':board
    }
    return render(request, 'art/full_art_result.html', context)

class ArtEdit(UpdateView):
    model = Art
    form_class = EditArtForms
    template_name = 'art/edit_result.html'
    success_url = reverse_lazy('Art')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (ArtEdit, self).form_valid(form)


class CreateArtResult(CreateView):
    model = Art
    form_class = ArtForms
    template_name = 'art/create_result.html'
    success_url = reverse_lazy('Art')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['class_of'].queryset = ArtAlbums.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (CreateArtResult, self).form_valid(form)

class CreateArtAlbums(CreateView):
    model = ArtAlbums
    fields = ['name']
    template_name = 'art/create_album.html'
    success_url = reverse_lazy('Art')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (CreateArtAlbums, self).form_valid(form)








def secondary_result_albums(request):
    reults = ScienceAlbums.objects.filter(user=request.user)
    context = {
        'results':reults
    }
    return render(request, 'resultSecondary/secondary_result.html', context)

def result_view_secondary(request, pk):
    post = get_object_or_404(ScienceAlbums, id=pk)

    result = ScienceAlbums.objects.get(id=pk)

    all_results = Science.objects.filter(class_of_id=result.pk)

    context = {
        'post':post,
        'result':result,
        'all_results':all_results
    }
    return render(request, 'resultSecondary/result_view.html', context)

class ResultSecondaryCreate(CreateView):
    model = Science
    form_class = ScineceForms
    template_name = 'resultSecondary/create_result_secondary_student.html'
    success_url = reverse_lazy('Home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['class_of'].queryset = ScienceAlbums.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (ResultSecondaryCreate, self).form_valid(form)

class ResultCreateSecondaryAlbum(CreateView):
    model = ScienceAlbums
    fields = ['name']
    template_name = 'resultSecondary/create_result_albums.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (ResultCreateSecondaryAlbum, self).form_valid(form)
