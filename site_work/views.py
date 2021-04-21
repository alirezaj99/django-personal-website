from django.shortcuts import render
from django.views.generic import ListView
from .models import Works
from site_work_category.models import WorksCategory


class WorkList(ListView):
    template_name = "work/work_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Works.objects.get_active_work()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = WorksCategory.objects.all()
        context["category"] = category

        return context
