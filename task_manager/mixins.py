from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy


class FormValidMixin:

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class FormContextMixin:
    h1 = None
    submit_button = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h1'] = self.h1
        context['submit_button'] = self.submit_button
        if getattr(self, 'get_delete_warning', None):
            context['delete_warning'] = self.get_delete_warning()
        return context
    

class AuthRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login_user')

    def handle_no_permission(self):
        messages.error(self.request, self.not_auth_message)
        return super().handle_no_permission()


class OwnerAccessMixin(AuthRequiredMixin):
    def get_owner_id(self, pk):
        current_model = self.model
        if current_model.__name__ == 'User':
            return pk
        model_object = current_model.objects.get(id=pk)
        try:
            return model_object.author.id
        except AttributeError:
            return 'IncorrectId'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().handle_no_permission()
        pk = kwargs.get('pk')
        owner_id = self.get_owner_id(pk)
        if request.user.id != owner_id:
            messages.error(request, self.another_user_message)
            return redirect(self.access_denied_redirect)
        return super().dispatch(request, args, kwargs)
    

class FilterMixin:
    def get_form_params(self):
        """ Можно переопределить метод во view для данных нужной 
         вам формы.
          Должен возвращать словарь с параметрами фильтрации. """
        active_filters = {}
        for key, val in self.filter_form.cleaned_data.items():
            if val:
                active_filters[key] = int(val)        
        if active_filters.get('author_id'):
            active_filters['author_id'] = self.request.user.id
        return active_filters

    def filter(self):
        form_params = self.get_form_params()
        self.queryset = self.queryset.filter(**form_params)

    def get(self, request, *args, **kwargs):
        self.filter_form = self.filter_form(request.GET)
        self.filter_form.update_choices()
        self.filter_form.is_valid()
        self.filter()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filter_form
        return context
