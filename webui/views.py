from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from api.models import Hospital, OxygenSupplier, Med, Notice

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

# Pharmacy

class MedsView(LoginRequiredMixin, ListView):
    model = Med
    template_name = "webui/meds.html"
    ordering = ['-last_updated']

class MedsDetailView(LoginRequiredMixin, DetailView):
    model = Med
    template_name = "webui/meds_detail.html"

class MedsCreateView(LoginRequiredMixin, CreateView):
    model = Med
    fields = ['name','address','contact','other_contact','availablity','tags','remarks']
    template_name = "webui/meds_form.html"

class MedsUpdateView(LoginRequiredMixin, UpdateView):
    model = Med
    fields = ['name','address','contact','other_contact','availablity','tags','remarks']
    template_name = "webui/meds_form.html"

class MedsDeleteView(LoginRequiredMixin, DeleteView):
    model = Med
    success_url ='/meds'
    template_name = "webui/item_confirm_delete.html"

# Help Desk

class NoticeView(LoginRequiredMixin, ListView):
    model = Notice
    template_name = "webui/notice.html"
    ordering = ['-last_updated']

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    fields = ['title','remarks','link']
    template_name = "webui/notice_form.html"

class NoticeUpdateView(LoginRequiredMixin, UpdateView):
    model = Notice
    fields = ['title','remarks','link']
    template_name = "webui/notice_form.html"

class NoticeDeleteView(LoginRequiredMixin, DeleteView):
    model = Notice
    success_url ='/notice'
    template_name = "webui/item_confirm_delete.html"
