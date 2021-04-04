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




class AdminDashboardView(TemplateView):

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





class ClientRequiredMixin(object):

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['org'] = Organization.objects.first()

        return context




class ClientIndexView(ClientRequiredMixin,TemplateView):

    template_name = 'clienttemplates/home.html'


class ClientContactUsView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/contactus.html'