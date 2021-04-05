from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.views.generic import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
import datetime

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mass_mail,send_mail
import json
from django.core import mail
from django.http import JsonResponse
# import requests
from django.contrib import messages



class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        # if request.user.is_authenticated and request.user.groups.filter(name="Admin").exists():
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/admin-site/login/?next=' + request.path)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['org'] = Organization.objects.first()

        return context



class AdminDashboardView(AdminRequiredMixin,TemplateView):

    template_name = 'admintemplates/dashboard.html'




class AdminLoginView(FormView):
    template_name = "admintemplates/admintemplate.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("fweanapp:adminindexpage")


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password = password)

        print(user)
        if user is not None :
            login(self.request,user)
        else:
            return render(self.request, self.template_name,{
                'form' : form,
                'error' : 'invalid credentials'
            })
        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET['next']
        else:
            return self.success_url






class AdminOrganizationCreateView(CreateView):
    template_name = 'admintemplates/organizationadd.html'
    # print(Organization.objects.all())
    model = Organization
    form_class = OrganizationForm
    success_url = reverse_lazy("fweanapp:admindashboard")



class AdminOrganizationUpdateView(AdminRequiredMixin,UpdateView):
    template_name = 'admintemplates/organizationadd.html'
    model = Organization
    form_class = OrganizationForm
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminorganizationdetail', kwargs={'pk': self.kwargs['pk']})


class AdminOrganizationDetailView(AdminRequiredMixin,DetailView):
    template_name = 'admintemplates/organizationdetail.html'
    model = Organization



from django.http import HttpResponse, HttpResponseRedirect
class ImageAlbumAddView(AdminRequiredMixin, CreateView):
    model = ImageMedia
    form_class = ImageAlbumForm
    template_name = 'admintemplates/imagealbumadd.html'
    success_url = reverse_lazy('fweanapp:admindashboard')

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        imagemedia_form = ImageMediaFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form = imagemedia_form,
                                  ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        imagemedia_form = ImageMediaFormSet(self.request.POST , self.request.FILES )
        # print(imagemedia_form.cleaned_data)

        if (form.is_valid() and imagemedia_form.is_valid()):
            return self.form_valid(form, imagemedia_form)
        else:
            return self.form_invalid(form, imagemedia_form)

    def form_valid(self, form, imagemedia_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        # print('=======')
        # print(self.object)
        self.object = form.save()
        imagemedia_form.instance = self.object
        # print('=======')
        # print(self.object)
        imagemedia_form.save()


        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, imagemedia_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form=imagemedia_form))



class ImageAlbumUpdateView(AdminRequiredMixin, UpdateView):
    model = ImageAlbum
    form_class = ImageAlbumForm
    formset_class = ImageMediaFormSet
    is_update_view = True
    template_name = 'admintemplates/imagealbumadd.html'
    success_url = reverse_lazy('adventureapp:adminhome')

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        album = ImageAlbum.objects.get(pk=kwargs.get('pk'))
        # print(album)

        imagemedia_form = ImageMediaFormSet(instance = album)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form=imagemedia_form,
                                  ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        album = ImageAlbum.objects.get(pk=kwargs.get('pk'))
        imagemedia_form = ImageMediaFormSet(self.request.POST , self.request.FILES, instance = album )
        print(imagemedia_form.cleaned_data)

        if (form.is_valid() and imagemedia_form.is_valid()):
            return self.form_valid(form, imagemedia_form)
        else:
            return self.form_invalid(form, imagemedia_form)

    def form_valid(self, form, imagemedia_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        # print('=======')
        # print(self.object)
        self.object = form.save()
        imagemedia_form.instance = self.object
        # print('=======')
        # print(self.object)
        imagemedia_form.save()


        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, imagemedia_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form=imagemedia_form))


class ImageMediaDeleteView(AdminRequiredMixin, DeleteView):
    model = ImageMedia
    template_name = 'admintemplates/imagemediadelete.html'
    success_url = reverse_lazy('adventureapp:adminhome')



class ImageAlbumListView(AdminRequiredMixin, ListView):
    model = ImageAlbum
    context_object_name = 'albums'

    template_name = 'admintemplates/imagealbumlist.html'



class ImageAlbumDetailView(AdminRequiredMixin, DetailView):
    model = ImageAlbum
    template_name = 'admintemplates/imagealbumdetail.html'
    success_url = reverse_lazy('adventureapp:adminimagealbumlist')

    context_object_name = 'albumdetail'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['imagemedias'] = ImageMedia.objects.filter(album__id=self.kwargs.get('pk'))

        return context



class ImageAlbumDeleteView(AdminRequiredMixin, DeleteView):
    model = ImageAlbum
    # template_name = 'admintemplates/adminimagealbumdelete.html'
    success_url = reverse_lazy('adventureapp:adminimagealbumlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)






#Client views

class ClientRequiredMixin(object):

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['org'] = Organization.objects.first()

        return context




class ClientIndexView(ClientRequiredMixin,TemplateView):

    template_name = 'clienttemplates/home.html'


class ClientContactUsView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/contactus.html'