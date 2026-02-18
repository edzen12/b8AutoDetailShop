from django.views.generic import (
    TemplateView, ListView, DetailView, 
    DeleteView, CreateView)


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
