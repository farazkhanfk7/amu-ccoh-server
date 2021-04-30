from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from api.models import Hospital, OxygenSupplier

# Create your views here.

def home(request):
    return render(request,'index.html')

class HospitalView(LoginRequiredMixin, ListView):
    model = Hospital
    template_name = "webui/hospitals.html"
    ordering = ['-last_updated']

class HospitalDetailView(LoginRequiredMixin, DetailView):
    model = Hospital
    template_name = "webui/hospital_detail.html"

class HospitalCreateView(LoginRequiredMixin, CreateView):
    model = Hospital
    fields = ['name','address','contact','other_contact','availablity','tags','remarks']
    template_name = "webui/hospital_form.html"

class HospitalUpdateView(LoginRequiredMixin, UpdateView):
    model = Hospital
    fields = ['name','address','contact','other_contact','availablity','tags','remarks']
    template_name = "webui/hospital_form.html"

class HospitalDeleteView(LoginRequiredMixin, DeleteView):
    model = Hospital
    success_url ='/hospitals'
    template_name = "webui/item_confirm_delete.html"

# Oxygen Supplier Views

class OxygenView(LoginRequiredMixin, ListView):
    model = OxygenSupplier
    template_name = "webui/oxygen.html"
    ordering = ['-last_updated']

class OxygenDetailView(LoginRequiredMixin, DetailView):
    model = OxygenSupplier
    template_name = "webui/oxygen_detail.html"

class OxygenCreateView(LoginRequiredMixin, CreateView):
    model = OxygenSupplier
    fields = ['name','address','contact','other_contact','availablity','type_is','remarks']
    template_name = "webui/oxygen_form.html"

class OxygenUpdateView(LoginRequiredMixin, UpdateView):
    model = OxygenSupplier
    fields = ['name','address','contact','other_contact','availablity','type_is','remarks']
    template_name = "webui/oxygen_form.html"

class OxygenDeleteView(LoginRequiredMixin, DeleteView):
    model = OxygenSupplier
    success_url ='/oxygen'
    template_name = "webui/item_confirm_delete.html"

