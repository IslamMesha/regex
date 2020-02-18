import re

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView

from entries.forms import EntryForm
from entries.models import Entry


class HomeView(TemplateView):
    template_name = 'home.html'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)


class EntryListView(TemplateView):
    template_name = 'list.html'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def get(self, request, *args, **kwargs):
        user = request.user
        context = self.get_context_data(**kwargs)
        entries = Entry.objects.filter(user=user).order_by('-date_added')
        matches = (self._parse_entry(entry) for entry in entries)
        context['entries'] = list(zip(entries, matches))
        return self.render_to_response(context=context)

    @staticmethod
    def _parse_entry(entry):
        match = re.search(entry.pattern, entry.test_string)
        if match is not None:
            return (
                match.group(),
                match.groups() or None,
                match.groupdict() or None,
            )
        return None


class EntryFormView(SuccessMessageMixin, FormView):
    form_class = EntryForm
    template_name = 'insert.html'
    success_url = reverse_lazy('insert')
    success_message = 'Entry was created successfully.'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def get(self, request, *args, **kwargs):
        return super(EntryFormView, self).get(request, *args, **kwargs)

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def post(self, request, *args, **kwargs):
        return super(EntryFormView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        self._save_with_user(form)
        return super(EntryFormView, self).form_valid(form)

    def _save_with_user(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
