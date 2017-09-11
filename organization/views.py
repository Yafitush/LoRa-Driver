from .models import Organization
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'organization/index.html'
    context_object_name = 'organization_list'

    def get_queryset(self):
        return Organization.objects.all()


class DetailView(generic.DetailView):
    model = Organization
    template_name = 'organization/detail.html'


class OrganizationCreate(CreateView):
    model = Organization
    fields = ['name', 'organization_type', 'country', 'logo']


class OrganizationUpdate(UpdateView):
    model = Organization
    fields = ['name', 'organization_type', 'country', 'logo']


class OrganizationDelete(DeleteView):
    model = Organization
    success_url = reverse_lazy('organization:index')

